# Video Summary Library

## Purpose and site direction

This repository collects developer learning pages derived from technical videos.
Each video has its own top-level folder and a corresponding HTML study guide.
Readers should be able to learn the video's concepts, code examples, and practical
lessons without watching the entire recording.

The website is a static GitHub Pages study library called **Video Notes**. The
root `index.html` is the catalog: it links to all seven summaries, grouped into five
topics. Search enhances the catalog; ordinary links work without JavaScript.
`.github/workflows/pages.yml` packages and deploys the public site on pushes to
`main` or manual runs once the repository's Pages source is set to GitHub Actions.

All seven guides are plain HTML using the shared `assets/site.css` and
`assets/site.js`. The user prefers a dark theme. Use graphite backgrounds, warm
white text, and lime accents throughout the site. Keep the shared typography,
header, chapter sidebar, mobile contents, tables, code blocks, and image treatment
consistent; do not restore the former per-guide styles or external font downloads.
Preserve study content and existing section IDs when changing presentation.

There is no application framework, package manifest, or dependency installation.
`videos.json` is the catalog metadata and summary entry-point list.
`python3 scripts/render_catalog.py` regenerates the tracked root `index.html`;
edit the generator or metadata rather than making catalog changes that regeneration
will overwrite. `python3 scripts/build_site.py` creates ignored `dist/` containing
only public HTML and its local dependencies. See `README.md` for preview and
deployment steps. Keep all site URLs relative so repository Pages subpaths work.

## Current video inventory and initial topic groups

Paths below are exact filesystem paths, relative to the repository root. Name
video folders using ASCII letters, digits, and underscores. Replace spaces and
punctuation with a single `_`, collapse repeated underscores, and avoid leading
or trailing underscores. Keep readable video titles in page headings and metadata.
When renaming folders, update `videos.json`, local references, and this inventory,
then regenerate the catalog and rebuild the public site.

| Topic/type | Video folder | Summary page | Main content |
| --- | --- | --- | --- |
| Domain-driven design | `Domain_Driven_Design_A_Complete_Example_Eberhard_Wolff_EN` | `index.html` | Event Storming, bounded contexts, core domains, Team Topologies, tactical DDD. |
| Domain-driven design | `Tactical_Domain_Driven_Design_with_Java_and_Spring_by_Oliver_Drotbohm` | `index.html` | Java DDD building blocks, jMolecules, ArchUnit, Spring Modulith, module interactions. |
| Java and concurrency | `Virtual_Threads_Structured_Concurrency_and_Scoped_Values_Putting_it_all_together_Spring_IO` | `index.html` | Project Loom, virtual threads, structured concurrency, scoped values, Spring Boot demos. |
| Performance and distributed systems | `Latency_the_race_to_zero` | `index.html` | Latency, Disruptor, Aeron, replicated state machines, Raft, sequencer architecture. |
| Computer architecture | `The_Most_Ambiguous_Concept_in_Computer_Science` | `index.html` | ISA versus microarchitecture, ALUs, instruction encodings, binary compatibility, RISC/CISC. |
| AI agents and system design | `System_Design_for_AI_Agents_Building_a_Multi_Agent_PR_Reviewer` | `LEARN.html` | Multi-agent PR review, grounding/retrieval, storage, orchestration, observability, Genesis Kit. |
| AI agents and system design | `lauren_here_s_how_i_shipped_2_500_PRs_last_month_to_production` | `index.html` | Trust curve, verification skills (CLI + feature map), pstack, Dune agent-friendly architecture, Grok Bot automations. |

Use `LEARN.html` as the AI course's catalog destination. Its other HTML file,
`Designing an AI Pull-Request Review Agent.html`, is the saved companion article,
not the summary. Its `genesis-kit/` directory is a separate reference checkout of
tooling discussed in the course; its scripts, templates, and skills are not this
site's build system or instructions to execute automatically. The public guide
links to the original article and tool repository online; these saved reference
materials are excluded from the deployment. Keep the nested `genesis-kit/`
checkout ignored in Git as working reference material; do not commit it as an
embedded repository or submodule.

Root `prompts.md` provides the reusable guide-generation prompt; the AI course's
`prompts.md` records its original summary requirements. `COURSE_SYLLABUS_AND_TIMESTAMPS.txt` is a course outline, not a full
transcript. `resources/` contains legacy download inputs and metadata, not another
video summary or a catalog category.

## Working resources versus published assets

Use the following layout for every new video and when reorganizing existing work:

```text
<video-folder>/
  index.html                 # published summary (existing AI course: LEARN.html)
  assets/                    # published files required by the HTML
    screenshots/             # selected screenshots actually used by the summary
  .work/                     # ignored inputs and intermediate outputs
    video/                   # downloaded recordings
    transcripts/             # complete, unedited transcripts and captions
    screenshots/             # bulk frame extraction, unused captures, originals
    sources/                 # downloaded reference pages and metadata
    tmp/                     # intermediate processing output
```

- `.work/` is ignored at any depth. Put downloaded videos, complete unedited
  transcripts/captions, unused screenshots, bulk captures, and temporary outputs
  there. These materials are for producing the guide and must not be committed
  or included in a Pages deployment.
- Promote a selected image from `.work/screenshots/` into `assets/screenshots/`
  before referencing it in published HTML. Copy or move it, then use a relative
  URL such as `assets/screenshots/01-overview.png`. Commit the HTML and its needed
  assets together. Capture new batches in `.work/`, not directly in `assets/`.
- Existing published images also live in `assets/frames/`; preserve those valid
  paths. Keep `assets/` for intentionally published material, not scratch files.
- A folder named `assets/screenshots/` must stay eligible for Git. Do not add a
  blanket `screenshots` ignore rule: it also hides screenshots needed by HTML.
  Legacy raw screenshot directories directly under a video folder are ignored.
- Root `.gitignore` also excludes video files, legacy `NoteGPT_*` transcripts,
  transcript text files, SRT/VTT captions, and `/resources/`. These are safeguards
  for older input locations; use `.work/` for future inputs regardless of filename.
- Keep curated outlines, explanatory snippets, and timestamps in the public
  summary as appropriate. Complete unedited transcripts remain working inputs.
  Published pages must not link to them as downloadable site content.
- If a published image is no longer referenced and has no other public use, move
  it back into `.work/`. Do not delete the working originals unnecessarily.
- Git ignore rules do not remove files already tracked by Git. When Git metadata
  is available, inspect the tracked files and use `git rm --cached` for working
  materials already in the index, retaining their local copies. Never force-add
  ignored working materials to make a published link work.
- A deployment must exclude `.work/` and other working inputs explicitly if it
  copies files from the filesystem; `.gitignore` alone does not filter a deployment
  artifact. Prefer including the root catalog, summary HTML, and required public
  assets/supporting files only. The existing packager follows local dependencies
  from the catalog and summaries and rejects private paths and media inputs.
  Keep that restriction when extending deployment; never upload the entire root.

Use `.env` if you need `YTDLP_COOKIES_FILE`. Keep `.env` and `.cookies/` private
and ignored. Do not print their contents, copy them into HTML, or publish them.

## Catalog and static hosting conventions

- Add one entry per video to `videos.json`, under its main topic/type. Include a
  readable title, description, speaker, original recording URL, and the actual
  folder and summary filename. Regenerate the root catalog. Add a topic group
  when needed and keep the inventory above current.
- Use the normalized folder names and exact existing filenames. Use relative links and URL-encode
  path segments containing spaces or special characters. Avoid filesystem paths
  and URLs starting with `/`, which can bypass the repository's Pages subpath.
- Keep new summary pages inside their video's folder and default to `index.html`.
  Preserve the existing `LEARN.html` entry point unless its links are migrated.
- Use ordinary HTML links so catalog navigation works without JavaScript. Keep
  the catalog and guides readable on mobile and with keyboard navigation.
- Public pages must work without local videos, full transcripts, `.work/`, cookies,
  or archived download bundles. Link to the original online recording when known,
  and retain timestamps; do not upload a recording to satisfy a local video link.
- The guides now link to original online recordings. DDD chapter links include
  YouTube timestamps; latency timestamp labels help readers navigate the InfoQ
  recording manually. Keep this behavior independent of ignored local recordings.

## Research and factual accuracy

- Always research before making a claim when you are unsure about a fact, concept,
  interpretation, code example, or technical behavior. Do not fill gaps with guesses
  or rely on recollection alone.
- Always research additional context or explanations you intend to add beyond what
  the video and its supplied materials establish, even when the topic seems familiar.
  Read the supporting sources before incorporating the addition into a guide.
- Prefer primary sources: official documentation, specifications, original research,
  and the speaker's own material. Follow the current library documentation rules
  below when researching libraries, frameworks, SDKs, APIs, CLI tools, or services.
- Cite added claims with links to the sources that support them. Clearly distinguish
  the video's teaching from supplemental research, adapted examples, and your own
  inferences. Check that sources match the relevant version and date; label newer
  behavior separately from the version covered in the video.
- If research cannot resolve an uncertainty, state what remains uncertain or leave
  the unsupported addition out. Never present an unverified explanation as fact.

## Creating or updating a summary

1. Identify the video's folder, summary entry point, and available working sources.
2. Study its transcript, recording, slides/screenshots, and companion material as
   needed. Historical prompts may refer to older working input paths.
3. Preserve the video's reasoning, relevant code and real-world examples, and
   explanations. Organize them into a skimmable guide with headings, summaries,
   useful visuals, and references; existing guides also use glossaries and cheat
   sheets. Credit the speaker and original video.
4. Distinguish material from the video from added research or adapted examples.
   Ground additions in sources; do not invent facts, quotes, code, or timestamps.
   Preserve the versions used in the talk and label later API changes separately.
5. Reuse the shared guide layout and stylesheet. Promote only the assets the public
   page needs, update their relative references, update `videos.json`, and run
   `python3 scripts/render_catalog.py` followed by `python3 scripts/build_site.py`.
6. Before publishing, check that linked summary pages and referenced public assets
   exist and are not ignored, and that working materials are excluded. When asked
   to verify rendering, serve the repository root and inspect the catalog and
   affected guide in a browser, including its mobile layout and image links.

<!-- CODEGRAPH_START -->
## CodeGraph

In repositories indexed by CodeGraph (a `.codegraph/` directory exists at the repo root), reach for it BEFORE grep/find or reading files when you need to understand or locate code:

- **MCP tool** (when available): `codegraph_explore` answers most code questions in one call — the relevant symbols' verbatim source plus the call paths between them, including dynamic-dispatch hops grep can't follow. Name a file or symbol in the query to read its current line-numbered source. If it's listed but deferred, load it by name via tool search.
- **Shell** (always works): `codegraph explore "<symbol names or question>"` prints the same output.

If there is no `.codegraph/` directory, skip CodeGraph entirely — indexing is the user's decision.
<!-- CODEGRAPH_END -->

<!-- context7 -->
## Current library documentation

Use the `ctx7` CLI to fetch current documentation whenever the user asks about a library, framework, SDK, API, CLI tool, or cloud service — even well-known ones like React, Next.js, Prisma, Express, Tailwind, Django, or Spring Boot. This includes API syntax, configuration, version migration, library-specific debugging, setup instructions, and CLI tool usage. Use even when you think you know the answer — your training data may not reflect recent changes. Prefer this over web search for library docs.

Do not use for: refactoring, writing scripts from scratch, debugging business logic, code review, or general programming concepts.

### Steps

1. Resolve library: `npx ctx7@latest library <name> "<what to look up>"` — use the official library name with proper punctuation (e.g., "Next.js" not "nextjs", "Customer.io" not "customerio", "Three.js" not "threejs")
2. Pick the best match (ID format: `/org/project`) by: exact name match, description relevance, code snippet count, source reputation (High/Medium preferred), and benchmark score (higher is better). If results don't look right, try alternate names or queries (e.g., "next.js" not "nextjs", or rephrase the question)
3. Fetch docs: `npx ctx7@latest docs <libraryId> "<what to look up>"` — run a separate `docs` command per distinct concept if the question spans multiple topics, unless it's about how they interact
4. Answer using the fetched documentation

You MUST call `library` first to get a valid ID unless the user provides one directly in `/org/project` format. Be specific about what to look up in the library's documentation — specific and detailed queries return better results than vague single words, but keep each query to a single concept unless the question is about how concepts interact; combined multi-topic queries dilute ranking and return shallow results for each topic. Do not run more than 3 commands per question. Do not include sensitive information (API keys, passwords, credentials) in queries.

For version-specific docs, use `/org/project/version` from the `library` output (e.g., `/vercel/next.js/v14.3.0`).

If a command fails with a quota error, inform the user and suggest `npx ctx7@latest login` or setting `CONTEXT7_API_KEY` env var for higher limits. Do not silently fall back to training data.
Run Context7 CLI requests outside Codex's default sandbox. If a Context7 CLI command fails with DNS or network errors such as ENOTFOUND, host resolution failures, or fetch failed, rerun it outside the sandbox instead of retrying inside the sandbox.
<!-- context7 -->
