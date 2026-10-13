# Video study guide prompt

Replace `<video-folder>` with the target folder, then give the prompt below to the
agent. Paths in the prompt are relative to the repository root.

```text
Create a complete developer study guide for the video in @<video-folder>/.
Its recording, full transcript, and other working materials are in `.work/`;
also inspect any legacy input locations described in AGENTS.md.

Goal
Produce a self-contained HTML guide that lets developers understand and apply
the video's teaching without watching the entire recording. Preserve its
substantive concepts, reasoning, examples, tradeoffs, and caveats. Make it easy
both to study carefully and to revisit a specific detail later.

1. Understand the source material
- Read the repository's AGENTS.md and inspect the target folder before editing.
  Identify the recording, transcript, available slides, companion materials,
  original video URL, and any existing guide.
- Read the entire transcript and examine the recording's audio and visuals.
  Inspect slides, diagrams, code demonstrations, and transitions that the
  transcript alone cannot explain. Work through long recordings in sections;
  do not infer the whole video from a few sampled frames or its opening minutes.
- Keep a coverage outline in `.work/tmp/` mapping the main topics, examples,
  demonstrations, and available timestamps to the guide's sections. Use it to
  avoid omitting material from later parts of the video.
- Treat transcripts as potentially inaccurate. Resolve terminology, code, and
  ambiguous statements against the recording or authoritative sources.
- If a source is missing, unreadable, or cannot be inspected with available
  tools, report the limitation accurately. Never claim to have watched or
  verified material you could not access.

2. Turn the video into a useful learning guide
- Start with the title, speaker, original recording link, a concise overview,
  intended audience, prerequisites, and what the reader will learn. Include
  only metadata supported by the available sources.
- Provide a linked table of contents and a coherent progression of chapters.
  You may reorganize the talk for clarity, but preserve its reasoning and
  meaningful connections between topics.
- Explain each major concept in plain language: what it means, why it matters,
  how it works, and when to use it. Include the speaker's assumptions, limits,
  alternatives, failure cases, and tradeoffs where discussed.
- Preserve every substantive code example, real-world example, and demo.
  Introduce the problem, explain the relevant code or steps, and describe the
  result and lesson. Consolidate repetitive demo edits only when their changes
  and purpose remain clear. Label incomplete snippets and omitted boilerplate;
  do not present reconstructed code as an exact transcription.
- Keep code selectable in HTML code blocks with readable formatting and a
  language label. Preserve the versions and APIs used in the talk. Explain
  corrections or adaptations explicitly rather than silently changing them.
- Use screenshots when they teach something: a diagram, important slide,
  interface state, or demo result. Add descriptive alt text and a caption
  explaining what to notice. Include a verified timestamp when available.
  Explain visual information in nearby text, and transcribe important code
  rather than making the reader decipher it in an image.
- Add concise chapter takeaways and a final recap or cheat sheet. Include a
  glossary, comparisons, or review questions when they help this particular
  subject; avoid padding and repetitive summaries.
- Include verified chapter or example timestamps so readers can revisit the
  original recording. Link to online timestamps where supported; never invent
  timestamps or depend on a local recording for navigation.

3. Research and attribute additions
- Always research anything you are unsure about before stating it as fact.
  Also research any extra context, explanation, or example you add beyond what
  the video and supplied materials establish, even if the subject is familiar.
- Read primary sources such as official documentation, specifications, original
  research, or the speaker's own material. Follow AGENTS.md's documentation
  lookup rules. Cite supporting source links beside the added explanation.
- Clearly distinguish the video's teaching from supplemental research,
  adapted examples, and your own inferences. Keep additions relevant to
  understanding the video rather than expanding into an unrelated tutorial.
- Check version and date compatibility. Label later API changes or newer
  guidance separately from what the speaker demonstrated.
- Never invent facts, quotations, benchmark results, code output, or source
  links. If evidence cannot resolve an uncertainty, state the uncertainty or
  omit the unsupported addition.

4. Build the page within this repository
- Place the guide at `<video-folder>/index.html`. If updating an existing guide,
  preserve its entry point and existing section IDs unless references are
  migrated deliberately. Keep useful existing content.
- Reuse the shared `assets/site.css` and `assets/site.js`, with relative paths
  from the guide, and the established guide layout. Use the site's dark theme,
  chapter sidebar, mobile contents, and link back to the root library.
- Use semantic HTML, readable headings, accessible navigation, and responsive
  tables, images, and code blocks. The content and ordinary navigation links
  must remain usable without JavaScript. Avoid external font dependencies.
- Keep recordings, full unedited transcripts/captions, bulk screenshots,
  downloaded references, and intermediate files under `.work/`. Keep working
  originals; do not publish them or link to them from the public page.
- Promote only images used by the guide into `assets/screenshots/` inside the
  video folder. These published assets must remain eligible for Git. Preserve
  valid existing `assets/frames/` references. Never force-add ignored inputs.
- Use relative site URLs so the guide works on a GitHub Pages repository subpath.
  Follow AGENTS.md's underscore naming convention for any new video folders.

5. Add the guide to the library
- Add or update its entry in root `videos.json`, using accurate metadata and
  the actual guide path. Choose the most appropriate existing topic group;
  create a new group only when none fits. Avoid duplicate entries.
- Keep the video inventory in AGENTS.md current.
- Regenerate the root catalog with `python3 scripts/render_catalog.py`, then
  package the public site with `python3 scripts/build_site.py`. Update metadata
  or the generator rather than manually editing the generated root index.html.
- Review the coverage outline against the finished guide. Ensure public links
  and required assets exist, published images are not ignored, and the package
  excludes all working materials. Report any build failure or unresolved gap.

Deliver the completed guide, its required public assets, and catalog updates.
In your final response, link to the guide and briefly report coverage, added
research, build results, and any material source or inspection limitations.
```
