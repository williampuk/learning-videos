/* Optional enhancements. Catalog links and guide content work without JavaScript. */
(() => {
  const search = document.querySelector('#library-search');
  if (search) {
    const cards = [...document.querySelectorAll('.study-card')];
    const groups = [...document.querySelectorAll('.topic-group')];
    const count = document.querySelector('#result-count');
    const empty = document.querySelector('#empty-state');
    const filter = () => {
      const words = search.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
      cards.forEach(card => {
        const content = `${card.textContent} ${card.dataset.search || ''}`.toLowerCase();
        card.hidden = !words.every(word => content.includes(word));
      });
      groups.forEach(group => { group.hidden = !group.querySelector('.study-card:not([hidden])'); });
      const shown = cards.filter(card => !card.hidden).length;
      count.textContent = `${shown} ${shown === 1 ? 'guide' : 'guides'}`;
      empty.hidden = shown > 0;
    };
    search.addEventListener('input', filter);
    document.querySelector('#clear-search').addEventListener('click', () => { search.value = ''; filter(); search.focus(); });
    document.querySelectorAll('.topic-sidebar a').forEach(link => link.addEventListener('click', () => {
      search.value = ''; filter();
      document.querySelectorAll('.topic-sidebar a').forEach(a => a.classList.toggle('active', a === link));
    }));
  }

  const progress = document.querySelector('.reading-progress');
  if (progress) {
    const update = () => {
      const maximum = document.documentElement.scrollHeight - innerHeight;
      progress.style.width = `${maximum > 0 ? Math.min(100, scrollY / maximum * 100) : 100}%`;
      const headings = [...document.querySelectorAll('.guide-content h2[id], .guide-content h3[data-toc]')];
      const current = headings.filter(heading => heading.getBoundingClientRect().top <= 140).at(-1) || headings[0];
      document.querySelectorAll('.guide-toc a').forEach(link => {
        const active = current && link.hash === `#${current.id}`;
        link.classList.toggle('active', Boolean(active));
        if (active) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current');
      });
    };
    addEventListener('scroll', update, {passive: true});
    addEventListener('resize', update);
    update();
  }
  document.querySelectorAll('.mobile-contents a').forEach(link => link.addEventListener('click', () => { link.closest('details').open = false; }));

  // Answers remain visible without JS, and become disclosure buttons when enhanced.
  document.querySelectorAll('.qbtn').forEach((button, index) => {
    const answer = button.nextElementSibling;
    if (!answer) return;
    answer.id = answer.id || `quiz-answer-${index}`;
    answer.hidden = true;
    button.hidden = false;
    button.setAttribute('aria-controls', answer.id);
    button.setAttribute('aria-expanded', 'false');
    button.addEventListener('click', () => {
      answer.hidden = !answer.hidden;
      button.setAttribute('aria-expanded', String(!answer.hidden));
      button.textContent = answer.hidden ? 'Reveal answer' : 'Hide answer';
    });
  });
  const glossarySearch = document.querySelector('#glossSearch');
  if (glossarySearch) {
    glossarySearch.setAttribute('aria-label', 'Search glossary');
    glossarySearch.addEventListener('input', () => {
      const query = glossarySearch.value.toLowerCase();
      document.querySelectorAll('#glossList .gterm').forEach(term => { term.hidden = !term.textContent.toLowerCase().includes(query); });
    });
  }
  if (navigator.clipboard && window.isSecureContext) {
    document.querySelectorAll('.guide-content pre').forEach(pre => {
      let block = pre.closest('.code-wrap, .codeblock');
      if (!block) {
        block = document.createElement('div'); block.className = 'codeblock';
        pre.before(block); block.append(pre);
      }
      let header = block.querySelector('.code-head');
      if (!header) { header = document.createElement('div'); header.className = 'code-head'; header.textContent = 'Code example'; block.prepend(header); }
      if (!header.querySelector('.copy')) {
        const button = document.createElement('button'); button.type = 'button'; button.className = 'copy'; button.textContent = 'Copy'; button.setAttribute('aria-label', 'Copy code example'); header.append(button);
      }
    });
    document.querySelectorAll('.copy').forEach(button => {
      button.hidden = false;
      button.addEventListener('click', async () => {
        const code = button.closest('.code-wrap, .codeblock').querySelector('pre');
        try {
          await navigator.clipboard.writeText(code.textContent);
          button.textContent = 'Copied';
        } catch { button.textContent = 'Select code to copy'; }
        setTimeout(() => { button.textContent = 'Copy'; }, 2000);
      });
    });
  }
  // One accessible image viewer, with native Escape handling and focus restoration.
  const images = [...document.querySelectorAll('.guide-content figure img')];
  if (images.length && typeof HTMLDialogElement !== 'undefined') {
    const dialog = document.createElement('dialog');
    dialog.className = 'image-dialog';
    dialog.setAttribute('aria-label', 'Screenshot viewer');
    const close = document.createElement('button'); close.textContent = 'Close ×';
    const enlarged = document.createElement('img');
    dialog.append(close, enlarged); document.body.append(dialog);
    close.addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
    images.forEach(img => {
      const button = document.createElement('button'); button.type = 'button'; button.className = 'image-button';
      button.setAttribute('aria-label', `Enlarge: ${img.alt || 'video screenshot'}`);
      img.before(button); button.append(img);
      button.addEventListener('click', () => { enlarged.src = img.src; enlarged.alt = img.alt; dialog.showModal(); });
    });
  }
})();
