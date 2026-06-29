# MatrixCE_GUI

> TRITON FLASH-ATTENTION 2 & PAGED KV CACHE LAYER (Mathematical stub for Local H2O-Danube 500M/1.8B execution)

*Auto-generated 2026-06-28 23:51 from source — branch `master`, 229 Python modules, 334 other files.*

## Architecture

```
  README.md
  matrix_dash/
    Blueprint.md
    CHANGELOG.md
    PROJECT_LOG.md
    README.md
    ROADMAP.md
    src/
      main.py
      utils.py
  web/
    900_STEPS_SINGULARITY.md
    BRAIN_LOG.md
    BUDGET_CREDITS.md
    Blueprint.md
    CHANGELOG.md
    CLIDE_SPEC.md
    ENTERPRISE_INIT.p
    ENTERPRISE_PROJECT_SOP.md
    GEMINI.md
    GLOBAL_MASTER_POLICY.md
    H2O_MATRIX_SOP.p
    LOGOS_PURPOSE.md
    Downloads/
      DIRECTIONS.md
      text.txt
      txt.txt
    GAME_SUBSTRATE/
      mechanics/
        AGENT_LAYER.py
        CYBER_CANVAS_TUI.py
        DETERMINISTIC_PHYSICS.py
    H2OIDE/
      .gitignore
      Blueprint.md
      CHANGELOG.md
      DATA_FLOW.md
      ENTERPRISE_INIT.p
      GLOBAL_PEDAGOGY.md
      MATRIX_GUI_ROADMAP.md
      PEDAGOGY_90_STEP_ARCHITECTURE.md
      PEDAGOGY_LEDGER_DUMP.sql
      PROJECT_LOG.md
      PROMPT_GUIDE.md
      README.md
      skills/
        terminal.json
      teaching_sandbox/
        Blueprint.md
        CHANGELOG.md
        PROJECT_LOG.md
        README.md
        a.py
      training_lab/
        event_01aa7be7.json
        event_1264cda6.json
        event_162ca735.json
        event_64b3a0e7.json
        event_6cf45c46.json
      training_sandbox/
        Blueprint.md
        CHANGELOG.md
        PROJECT_LOG.md
        README.md
        ROADMAP.md
        gen_10_20260526_074241.md
        gen_1_20260525_233908.md
        gen_2_20260526_003908.md
        gen_3_20260526_013908.md
        gen_4_20260526_023908.md
        gen_5_20260526_033908.md
        ...
```

## Dependencies

External packages imported by this project:

`KAI_9000`, `MARKOV_ALGEBRAIC_FITNESS`, `PocketMatrix`, `apache_beam`, `asyncpg`, `bs4`, `cmd`, `core_brain`, `cryptography`, `dis`, `dotenv`, `email`, `evernote`, `fastapi`, `flask`, `genetic_flow`, `gkeepapi`, `joblib`, `kqml_protocol`, `markdown`, `mimetypes`, `mmap`, `numpy`, `openai`, `openrouter_manager`, `pandas`, `pydantic`, `pytest`, `rag_pipeline`, `rank_bm25`, `requests`, `rich`, `sklearn`, `smtplib`, `sqlalchemy`, `symbolic_brain`, `tarfile`, `unittest`, `xml`, `yaml`, `zipfile`

## How to run

Executable entry points (have a `__main__` block):

- `python web/GAME_SUBSTRATE/mechanics/AGENT_LAYER.py`
- `python web/GAME_SUBSTRATE/mechanics/CYBER_CANVAS_TUI.py`
- `python web/GAME_SUBSTRATE/mechanics/DETERMINISTIC_PHYSICS.py`
- `python web/H2OIDE/agy_python.py`
- `python web/H2OIDE/anti_hang_watchdog.py`
- `python web/H2OIDE/autonomous_engine.py`
- `python web/H2OIDE/cognitive_db.py`
- `python web/H2OIDE/daemon.py`
- `python web/H2OIDE/danube_logic_orchestrator.py`
- `python web/H2OIDE/genetic_optimizer.py`
- `python web/H2OIDE/h2o_cli_ide.py`
- `python web/H2OIDE/h2o_db_schema.py`

## Modules

### `web/GAME_SUBSTRATE/mechanics/AGENT_LAYER.py`

- `auto_configure(intent)` — Detects intent and changes system settings automatically.

### `web/GAME_SUBSTRATE/mechanics/DETERMINISTIC_PHYSICS.py`

- **class `StateMachine`**
  - methods: `process_input`, `update`

### `web/H2OIDE/agy_python.py`

- `get_openrouter_config()`
- `log_interaction(prompt, response)`
- `call_openrouter(prompt)`
- `main()`

### `web/H2OIDE/anti_hang_watchdog.py`

- `trigger_failover()`
- `execute_with_watchdog(func)` — Executes a function and returns a failover result if it hangs.

### `web/H2OIDE/autonomous_engine.py`

- `run_automated_tasks()`

### `web/H2OIDE/cognitive_db.py`

- `init_db()`

### `web/H2OIDE/daemon.py`

- `background_sync()`
- `run_ide()`

### `web/H2OIDE/danube_logic_orchestrator.py`

- **class `DanubeOrchestrator`**
  - methods: `run_ai`, `distill_intent`, `plan`, `save_tree`, `display_tree`, `execute_task`, `test_task`, `sync`, `run`

### `web/H2OIDE/fuzzy_logic_gate.py`

- `get_templates()`
- `calculate_jaccard_similarity(text1, text2)` — Algebraic overlap: |A intersection B| / |A union B|
- `match_predictive_topology(user_intent)` — Acts as a fuzzy logic gate. Maps the user intent to a specific topological

### `web/H2OIDE/genetic_optimizer.py`

- `prune_prompt(prompt_text, max_len)` — Prunes a prompt to keep only the highest density of instructional tokens.
- `hash_state(prompt)`
- `get_environmental_penalty()` — Reads system thermal limits for algebraic balancing.
- `fitness(response_text, duration)`
- `run_darwin_loop()`

### `web/H2OIDE/h2o_cli_ide.py`

- **class `H2OIDE`**
  - methods: `_call_model`, `default`, `do_exit`

### `web/H2OIDE/h2o_db_schema.py`

- `init_layered_schema()`

### `web/H2OIDE/headless_project_suite.py`

- `get_state()`
- `update_state(key, value)`
- `set_roadmap(roadmap_steps)`
- `advance_step()`
- `inject_context(prompt)`

### `web/H2OIDE/initialize_enterprise_project.py`

- `get_token()`
- `generate_ascii_tree(path)` — ASCII tree generator.
- `initialize()`

### `web/H2OIDE/matrix_orchestrator.py`

- `print_topic_update(title, summary, intent)` — Mirrors the agentic topic update structure.
- `enforce_pacing()` — Ensures we do not exceed OpenRouter API ping limits.
- `run_cognitive_layer(prompt)` — Hits the OpenRouter API via aichat CLI.
- `run_execution_layer(plan)` — Extracts commands and uses Aider to implement changes.
- `run_sync_layer(message)` — Triggers the Github Operator to upload.
- `main()`

### `web/H2OIDE/network_hook.py`

- `webhook()`

### `web/H2OIDE/pedagogy_loop.py`

- `log_to_ledger(task, cmd)`
- `call_llm_agy(task)`
- `teach()`

### `web/H2OIDE/pedagogy_mirror_builder.py`

- `extract_api_key()`
- `generate_mirror(language, iteration, mutation_factor)` — Hits LiteLLM Gateway to generate a structural mirror in another language.
- `fitness_evaluation(code, language)` — Calculates fitness based on execution speed and string density.
- `run_100x_loop()`

### `web/H2OIDE/semantic_evolution.py`

- `simulate_llm_classification(prompt_template, user_input, context)` — Simulate an LLM reading the prompt and categorizing the input.
- `evolve()`

### `web/H2OIDE/slow_pedagogy_daemon.py`

- `throttle_cpu()`
- `check_lock()`
- `get_high_entropy_task()` — Step 11: Poll ledger.db for the most confusing recent task.
- `execute_pedagogy_cycle(generation)`

### `web/H2OIDE/training_lab_engine.py`

- **class `TritonChooserLab`**
  - methods: `load_weights`, `save_weights`, `triton_chooser_logic`, `run_permutation_event`, `save_event`

### `web/H2OIDE/triton_danube_kernel.py`

TRITON FLASH-ATTENTION 2 & PAGED KV CACHE LAYER
(Mathematical stub for Local H2O-Danube 500M/1.8B execution)

- **class `TritonPagedAttention`**
  - methods: `allocate_block`, `compute_flash_attention`
- **class `AsynchronousSampler`**
  - methods: `sample_logits`

### `web/PocketMatrix/system/agentic_sync_daemon.py`

- `log(msg)`
- `run_sync_cycle()`
- `main()`

### `web/PocketMatrix/system/apps/AgentConnections/app.py`

- `authenticate(phrase)`
- `establish_pipe(ip, port, proto, auth_phrase)`
- `get_telemetry()`

### `web/PocketMatrix/system/apps/ViperNote/app.py`

- `save_note(note_content, auth_phrase)`

### `web/PocketMatrix/system/backup/gui_bridge_LEGACY.py`

- `list_models()`
- `active_model()`
- `list_knowledge()`
- `search_knowledge()`
- `knowledge_stats()`
- `desktop()`
- `manifest()`
- `omni_chat()`
- `list_projects()`
- `list_databases()`
- `query_database()`
- `update_database()`
- `handle_notes()`
- `handle_todo()`
- `sync_todo_google()`

### `web/PocketMatrix/system/bm25_orchestrator.py`

BM25 Self-Learning Orchestrator
This orchestrator uses the BM25 algorithm to retrieve successful task patterns
from the memory ledger/database, allowing the system to "self-learn" and adapt
its prompts based on historically successful agent runs.

- **class `BM25Orchestrator`**
  - methods: `load_memory`, `_add_document`, `_compute_idf`, `get_scores`, `retrieve_best_context`, `orchestrate`

### `web/PocketMatrix/system/ce_simulator.py`

- **class `CESubstrateSimulator`** — Simulates a remote Windows CE device for local testing and pedagogy.
  - methods: `get_status`, `simulate_shell`

### `web/PocketMatrix/system/chat_harvester.py`

- `extract_todos()`

### `web/PocketMatrix/system/enex_importer.py`

- `import_enex(enex_file_path)`

### `web/PocketMatrix/system/evernote-gw-py/evernote_gw.py`

- `load_tokens()`
- `save_tokens(tok)`
- `enml_wrap(html_body)`
- `md_to_enml(md)`
- `md5_hex(b)`
- `get_client(token)`
- `cmd_auth(_args)`
- `cmd_create_note(args)`
- `cmd_import_jsonl(args)`
- `main()`

### `web/PocketMatrix/system/evernote_manager.py`

- `init_db()`
- `upsert_note(note_id, title, content, tags, updated_at)`
- `search_notes(query)`

### `web/PocketMatrix/system/fault_injector.py`

- **class `DynamicFaultInjector`**
  - methods: `inject_fault`, `tutor_student`

### `web/PocketMatrix/system/google_bridge.py`

- `load_credentials()` — Loads Google credentials (Email and App Password) from config.
- `send_gmail(to_addr, subject, body, retries)` — Sends an email via Gmail SMTP using an App Password with exponential backoff.
- `sync_keep(tasks, retries)` — Syncs the local PocketMatrix ToDo database with Google Keep with backoff.

### `web/PocketMatrix/system/gui_bridge.py`

- `list_models()`
- `active_model()`
- `list_knowledge()`
- `search_knowledge()`
- `knowledge_stats()`
- `desktop()`
- `manifest()`
- `omni_chat()`
- `list_projects()`
- `list_databases()`
- `query_database()`
- `update_database()`
- `handle_notes()`
- `handle_todo()`
- `sync_todo_google()`

### `web/PocketMatrix/system/harvest_evernote.py`

- `harvest_notes()`

### `web/PocketMatrix/system/harvest_logs.py`

- `harvest_logs()`

### `web/PocketMatrix/system/headless_bridge.py`

- **class `HeadlessBridge`**
  - methods: `translate_and_execute`

### `web/PocketMatrix/system/ingestion_engine.py`

- **class `IngestionEngine`**
  - methods: `clean_text`, `fetch_and_parse`, `format_for_danube`

### `web/PocketMatrix/system/knowledge_hub.py`

- `init_hub()`
- `search_knowledge_bm25(query)`

### `web/PocketMatrix/system/onedrive_scanner.py`

- `scan_and_ingest(scan_path)`

### `web/PocketMatrix/system/orchestrator.py`

- `get_active_todos()`
- `get_blueprints()`
- `run_orchestration()`

### `web/PocketMatrix/system/positive_ping.py`

- `generate_ping()`

### `web/PocketMatrix/system/project_to_evernote.py`

- `summarize_and_store()`

### `web/PocketMatrix/system/quarantine_filter.py`

- `isolate_anomalies()`

### `web/PocketMatrix/system/telemetry_parser.py`

- **class `TelemetryParser`**
  - methods: `generate_mock_telemetry`, `analyze_telemetry`

### `web/PocketMatrix/zero_to_ce/payload/download_weights.py`

- `download_model()`

### `web/PocketMatrix/zero_to_ce/payload/hypersync_engine.py`

- `sync_projects()`
- `thermal_governor()`

### `web/PocketMatrix/zero_to_ce/payload/init_databases.py`

- `init_db(name, schema)`

### `web/PocketMatrix/zero_to_ce/payload/local_file_indexer.py`

- `get_embedding(text)`
- `index_file(file_path)`
- `run_indexing()`

### `web/PocketMatrix/zero_to_ce/phase7_sync_v1/payload/conflict_resolver.py`

- `resolve_conflict(local_state, remote_state)` — State objects should have:

### `web/PocketMatrix/zero_to_ce/phase7_sync_v1/payload/inference_offload_router.py`

- `get_peer_ip()` — Retrieves the last known peer IP from state.
- `route_request(prompt, model)` — Routes a generation request.

### `web/PocketMatrix/zero_to_ce/phase7_sync_v1/payload/key_exchange.py`

- `generate_keys()` — Generates RSA keys if they do not exist.
- `sign_heartbeat()` — Signs a 'HEARTBEAT' message with the private key.
- `verify_node_ready(signature, public_key_pem)` — Verifies a 'NODE_READY' message using a provided public key.

### `web/PocketMatrix/zero_to_ce/phase7_sync_v1/payload/node_discovery.py`

- `start_discovery()`

### `web/PocketMatrix/zero_to_ce/phase7_sync_v1/payload/os_fingerprint.py`

- `get_thermal_status()` — Reads the primary thermal zone temperature.
- `get_total_ram()` — Reads total system memory from /proc/meminfo.
- `get_fingerprint()` — Returns a JSON-compatible dictionary of hardware specs.

### `web/PocketMatrix/zero_to_ce/phase8_pedagogy_v1/payload/evolutionary_merger.py`

- `get_fitness_scores()` — Reads fitness scores from a JSON file.
- `calculate_mock_fitness(branch_name)` — Fallback: Mock fitness based on string complexity or file presence.
- `merge_fittest()` — Identifies the fittest branch and mocks the merge process.

### `web/PocketMatrix/zero_to_ce/phase8_pedagogy_v1/payload/genetic_crossover.py`

- `extract_function(content, func_name)` — Extracts a function definition and its body using regex.
- `perform_crossover(file1_path, file2_path, func_name)` — Swaps a function between two Python files.

### `web/PocketMatrix/zero_to_ce/phase8_pedagogy_v1/payload/shadow_executor.py`

- `setup_shadow()` — Ensures the shadow directory exists.
- `sync_minimal_payload(source_dir)` — Copies minimal files to shadow directory for execution.
- `execute_in_shadow(command)` — Runs a command inside the shadow directory.

### `web/PocketMatrix/zero_to_ce/phase9_ascent_v1/payload/pat_manager.py`

- `rotate_pat()`

### `web/PocketMatrix/zero_to_ce/phase9_ascent_v1/payload/self_refactor.py`

- `refactor()`

### `web/PocketMatrix/zero_to_ce/phase9_ascent_v1/payload/wisdom_harvester.py`

- `harvest()`

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/Triton_Danube_Bridge.py`

- `write_with_genetic_buffer(file_path, content)` — Writes to a file using the optimal 18KB chunking to prevent SQLite WAL locks.
- `triton_execute(performative, payload)`

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/action_recorder.py`

- `record_action(performative, success)`

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/action_sequencer.py`

- `process_queue()`

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/burn_in_tester.py`

- `generate_noise(length)`
- `run_burn_in()`

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/chat_template_pedagogy.py`

- `learn_from_chats()`

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/generate_cats_site.py`

- `generate_node(node_info, depth)`

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/genetic_pedagogy_engine.py`

- `init_db()`
- `calc_entropy(text)`
- `simulate_execution(entropy, threshold)` — Simulates latency based on routing path. Abstract LLM vs Symbolic Cache.
- `genetic_loop(generations, iterations_per_gen)`

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/genetic_project_simulator.py`

- `cleanup_test_dir()`
- `simulate_project_creation(buffer_size)`
- `genetic_loop()`

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/master_router.py`

- `load_learned_macros()` — Phase 15: Autonomously loads learned shorthand templates.
- `parse_intents(prompt)` — Splits multi-intent prompts (e.g. '1 then 2') into discrete sequences.
- `execute_route(prompt)`
- `main()`

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/mmap_cache.py`

- `get_mmap_cache()` — Returns the fast memory-mapped dictionary.
- `update_mmap_cache(new_dict)` — Writes the dictionary back to the RAM-fenced block.

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/modulator_engine.py`

- `calculate_weights()`
- `evolve_orchestrator()`

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/semantic_drift_pruner.py`

- `prune_stale_weights()`

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/shannon_router.py`

- `calculate_shannon_entropy(prompt)` — Calculates linguistic entropy to determine cognitive routing.
- `generate_predictive_hash(prompt)` — Algebraic hash to match historical successful trajectories.
- `route_request(prompt)`

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/task_distiller.py`

- `distill(request_text)`

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/upgrade_schemas.py`

- `upgrade_schema()`

### `web/PocketMatrix/zero_to_ce/self_modifying_orchestrator/payload/zipped_response_packer.py`

- `pack_response()`

### `web/_Archived_Root/scripts/CONTENT_ARCHITECT.py`

- **class `ContentArchitect`**
  - methods: `generate_blueprint`, `publish_blueprint`

### `web/_Archived_Root/scripts/ContentArchitect.py`

- **class `QualityContentEngine`**
  - methods: `_load_state`, `_save_state`, `is_unique`, `generate_page_metadata`

### `web/_Archived_Root/scripts/DUAL_COGNITIVE_ENGINE.py`

- **class `DualCognitiveEngine`**
  - methods: `extractor_layer`, `agent_symbolic`, `agent_neural`, `patch_response`, `process`

### `web/_Archived_Root/scripts/FINAL_TEST_PILOT.py`

- `test_no_refusal()`

### `web/_Archived_Root/scripts/FOUNDRY_MASTER.py`

- **class `SuccessVault`**
  - methods: `encrypt`, `decrypt`
- **class `FoundryMaster`**
  - methods: `harden_database`, `log_entropy_event`, `get_thermal_temp`, `thermal_guard`, `calculate_state_hash`, `calculate_entropy`, `markov_transition`, `module_talking`, `module_planning`

### `web/_Archived_Root/scripts/GENETIC_TUI.py`

- **class `GeneticTUI`**
  - methods: `get_latest_stats`, `get_thermal`, `make_layout`, `generate_table`, `run`

### `web/_Archived_Root/scripts/GH_SYNC_SERVICE.py`

- **class `GHSyncService`**
  - methods: `initialize_state`, `check_for_milestones`, `sync_to_github`, `routine`

### `web/_Archived_Root/scripts/H2O_BRIDGE.py`

- **class `H2OBridge`**
  - methods: `execute_remote`, `log_bridge_event`

### `web/_Archived_Root/scripts/HEADLESS_BRIDGE.py`

- **class `HeadlessBridge`**
  - methods: `send_command`

### `web/_Archived_Root/scripts/KQML_HANDOFF.py`

- **class `KQMLHandoff`**
  - methods: `delegate_inference`

### `web/_Archived_Root/scripts/MARKOV_DEBUGGER.py`

- **class `MarkovDebugger`**
  - methods: `draw_bar`, `view_recent_transitions`, `monitor`

### `web/_Archived_Root/scripts/PEDAGOGY_HARVESTER.py`

- `harvest()` — Autonomous Pedagogy Harvester

### `web/_Archived_Root/scripts/PEDAGOGY_SUPER_TRAINER.py`

- **class `PedagogyOrchestrator`**
  - methods: `generate_autonomous_plan`, `execute_scientific_cycle`, `git_sync`, `run_8_hour_routine`

### `web/_Archived_Root/scripts/PEDAGOGY_TRAINER.py`

- `train_pattern(task, correct_command)`

### `web/_Archived_Root/scripts/README_GENERATOR.py`

- **class `ReadmeGenerator`**
  - methods: `get_ascii_tree`, `get_roadmap_stats`, `get_thermal_health`, `generate`

### `web/_Archived_Root/scripts/SCIENTIFIC_EXECUTOR.py`

- `log_scientific_step(step_num, step_desc, observation, hypothesis, experiment, result)`
- `get_next_step()`
- `mark_step_complete(step_num)`
- `run_with_limits(command)`
- `execute_step(step_num, step_desc)`

### `web/_Archived_Root/scripts/SEED_VAULT.py`

- `seed_vault()`

### `web/_Archived_Root/scripts/SELF_HEALING.py`

- **class `SelfHealing`**
  - methods: `check_db_integrity`, `recover_from_freeze`, `attestation_loop`

### `web/_Archived_Root/scripts/STATE_FREEZER.py`

- **class `StateFreezer`**
  - methods: `freeze`, `list_freezes`

### `web/_Archived_Root/scripts/SUBSTRATE_ORGANIZER.py`

- **class `SubstrateOrganizer`**
  - methods: `rotate_logs`, `prune_backups`, `run`

### `web/_Archived_Root/scripts/SYMBOLIC_EXECUTOR.py`

- **class `DeterministicExecutor`**
  - methods: `run_test_iteration`, `verify_determinism`

### `web/_Archived_Root/scripts/SYNC_ONEDRIVE.py`

- **class `OneDriveSync`**
  - methods: `sync`

### `web/_Archived_Root/scripts/SubstrateOrganizer.py`

- `organize_and_tidy()`

### `web/_Archived_Root/scripts/TODO_SCANNER.py`

- `scan_todos()` — High-Fidelity Todo Scanner
- `cleanup_completed()` — Removes [x] tasks from substrate to keep entropy low.
- `update_syphon(all_todos)` — Injects aggregated todos into the CHAT_SYPHON.md manifest.

### `web/_Archived_Root/scripts/TODO_SYPHON.py`

- `extract_from_chats()`
- `update_syphon(new_todos)`

### `web/_Archived_Root/scripts/UPDATE_CHANGELOG.py`

- **class `ChangelogUpdater`**
  - methods: `get_recent_commits`, `run_inference`, `generate_summary`, `update`

### `web/_Archived_Root/scripts/VIPER_SCRAPER.py`

- **class `ViperScraper`**
  - methods: `scrape_kernel_data`, `export_to_wisdom`

### `web/_Archived_Root/scripts/agent_core.py`

- **class `MobileAgentBroker`**
  - methods: `update_project_map`, `get_compressed_context_tree`, `call_llm`, `execute_command`, `danube_chat_loop`, `triton_execution_loop`, `run`

### `web/_Archived_Root/scripts/agent_streaming.py`

- **class `MobileAgentBroker`**
  - methods: `call_llm_stream`

### `web/_Archived_Root/scripts/autonomous_master.py`

- `filter_and_route(text)`
- `run_loop()`

### `web/_Archived_Root/scripts/autonomous_training_loop.py`

- `training_cycle()`

### `web/_Archived_Root/scripts/complete_roadmap.py`

- `complete_roadmap(file_path)`

### `web/_Archived_Root/scripts/data_pipeline.py`

- `data_preprocessing(df)`
- `model_training(df)`
- `pipeline(df)`

### `web/_Archived_Root/scripts/data_scraper.py`

- `scrape_news_sources()`

### `web/_Archived_Root/scripts/db_analysis.py`

- `analyze_schema(db_name)`

### `web/_Archived_Root/scripts/engine_loop.py`

- `extract(text)`

### `web/_Archived_Root/scripts/genetic_optimizer.py`

- `fitness(response_text, duration)`

### `web/_Archived_Root/scripts/genetic_pro_trainer.py`

- `run_pro_github_genetic_test()`

### `web/_Archived_Root/scripts/handoff_engine.py`

- `execute_handoff(target_ip, target_path)`

### `web/_Archived_Root/scripts/horizon_executor.py`

- `run_horizon_step(step_id, domain, task)`
- `main()`

### `web/_Archived_Root/scripts/initialize_enterprise_project.py`

- `get_token()`
- `generate_ascii_tree(path)` — Simple ASCII tree generator.
- `generate_high_fidelity_readme(project_name, tree)`
- `initialize()`

### `web/_Archived_Root/scripts/local_singularity_harvester.py`

- `init_training_db()`
- `harvest_and_train()`

### `web/_Archived_Root/scripts/matrix_coordinator.py`

- **class `MatrixCoordinator`**
  - methods: `check_connectivity`, `get_thermal`, `export_trade_package`, `process_sync_queue`, `execute_swarm_trade`, `merge_foreign_notes`, `sync_ledger`, `routine`

### `web/_Archived_Root/scripts/module.py`

- **class `Calculator`**
  - methods: `calculate_result`
- **class `Processor`**
  - methods: `process_data`

### `web/_Archived_Root/scripts/parent_a.py`

- `core_logic()`

### `web/_Archived_Root/scripts/parent_a_OFFSPRING.py`

- `core_logic()`

### `web/_Archived_Root/scripts/parent_b.py`

- `core_logic()`

### `web/_Archived_Root/scripts/parent_b_OFFSPRING.py`

- `core_logic()`

### `web/_Archived_Root/scripts/perform_github_edit.py`

- `perform_edit()`

### `web/_Archived_Root/scripts/pipeline.py`

- `ingest_data()`
- `process_data(data)`
- `transform_data(data)`
- `store_data(data)`
- `ingest_data(file_path)`
- `preprocess_data(data)`
- `train_model(data)`
- `evaluate_model(model, data)`
- `deploy_model(model)`

### `web/_Archived_Root/scripts/predictive_wrapper.py`

- **class `PredictiveGuard`**
  - methods: `setup_db`, `get_mem_info`, `predict_fault`, `monitor_loop`, `mitigate`

### `web/_Archived_Root/scripts/run_recursive_validation_tests.py`

- `run_test(tid, prompt)`
- `main()`

### `web/_Archived_Root/scripts/scientific_orchestrator.py`

- `print_topic(title, summary, intent)`
- `run_aichat(prompt)` — Hits OpenRouter via the underlying aichat binary.
- `generate_docs(project_topic)`
- `execute_aider(prompt)`
- `setup_continue_workspace()`
- `upload_github()`
- `main()`

### `web/_Archived_Root/scripts/scraper.py`

- **class `NewsScraper`**
  - methods: `scrape`
- `main()`

### `web/_Archived_Root/scripts/scrub_engine.py`

- `scrub_output(text)` — [PERFORMATIVE: SCRUB] High-entropy prose extractor.

### `web/_Archived_Root/scripts/setup_pedagogy_routine.py`

- `verify_and_sync()`

### `web/_Archived_Root/scripts/singularity_evolution_engine.py`

- `print_epoch(epoch, range_val, description)`
- `evolve_trait(trait_name, code_file, code_content)`
- `main()`

### `web/_Archived_Root/scripts/singularity_test_harness.py`

- `log(msg)`
- `run_singularity_test(test_id, prompt)`
- `main()`

### `web/_Archived_Root/scripts/test_autonomous_edit.py`

- `test_edit()`

### `web/_Archived_Root/scripts/test_broker_direct.py`

- `run_test()`

### `web/_Archived_Root/scripts/test_deep_context.py`

- `simulate_deep_conversation()`

### `web/_Archived_Root/scripts/test_interaction.py`

- `test_interaction()`

### `web/_Archived_Root/scripts/test_module.py`

- **class `TestCalculator`**
  - methods: `test_calculate_result`
- **class `TestProcessor`**
  - methods: `test_process_data`

### `web/_Archived_Root/scripts/test_orchestrator.py`

- `run_orchestrated_task()`

### `web/_Archived_Root/scripts/test_step_16.py`

- `test_mutation_injection()`

### `web/_Archived_Root/scripts/train_runtime.py`

- `start_training_loop()`

### `web/_Archived_Root/scripts/triton_broker.py`

- **class `TritonBroker`**
  - methods: `_init_db`, `update_task_status`, `log_task`, `call_llm`, `execute_task`, `orchestrator_loop`

### `web/_Archived_Root/scripts/verify_node_visibility.py`

- `check_pings()`

### `web/app/main.py`

- **class `TestCoverage`**
- `get_test_coverage()`
- `calculate_coverage()`

### `web/genetic_flow/cluster/sync_hook.py`

- `sync_bayesian_weights()` — Bridge ledger.db quantum_parameters into the genetic flow loop.
- `export_optimization_stats()` — Export genetic progress back to the main IDE ledger.

### `web/genetic_flow/cluster/topology_mapper.py`

- `initialize_cluster_table()`
- `update_heartbeat(node_id)` — Updates the heartbeat for a specific cluster node.
- `get_cluster_topology()` — Returns a string representation of the cluster topology for the TUI.

### `web/genetic_flow/core_brain/binary_engine/decompiler.py`

- **class `BinaryDecompilationEngine`** — Airgapped processor that translates Python logic into binary opcode math.
  - methods: `decompile_and_score`

### `web/genetic_flow/core_brain/router.py`

- **class `LocalAgentRouter`** — [PERFORMATIVE: ROUTE] Native 32-bit llama-cli Wrapper with KQML/Vector Handoff.
  - methods: `get_management_rules`, `run_generation`, `clean_code`
- `extract_clean_code(raw_stream)`

### `web/genetic_flow/core_brain/target_feature.py`

- `algorithm(n)`

### `web/genetic_flow/core_brain/test_harness.py`

- **class `StatisticalEvaluator`** — [PERFORMATIVE: EVALUATE] Evaluates microsecond trends via IQR variance algorithms (Pure Python).
  - methods: `evaluate_performance`
- `evaluate()`

### `web/genetic_flow/core_brain/tui_layout.py`

- `get_last_insight()`
- `generate_dashboard(gen, fitness, code_str, stuck_count, max_stuck, sprite_status)`

### `web/genetic_flow/core_brain/watchdog.py`

- **class `Watchdog`**
  - methods: `check_stagnation`, `get_hyperparameter_adjustment`, `trigger_cloud_escalation`

### `web/genetic_flow/master_logic/gemini_agent.py`

- `get_embedding(text)`
- `fetch_memory_context(goal)`
- `run_cmd(cmd)`
- `fix_step(step_data, error_output, sys_constraints, decompiler, max_retries)`
- `main(goal)`

### `web/genetic_flow/memory_daemon/gemini_client.py`

- `send_to_daemon(command, exit_code)`

### `web/genetic_flow/memory_daemon/gemini_daemon.py`

- `process_and_store(payload)` — The heavy lifting she does silently after your terminal is already free.
- `handle_connection(reader, writer)` — Instantly accepts data from your shell hook and releases it.
- `main()`

### `web/genetic_flow/memory_pipeline/audio_engine.py`

- **class `AudioManifestationEngine`** — [PHASE 5.2/5.3] Headless TTS & Async Streaming Engine.
  - methods: `speak`, `run_audio_feedback`

### `web/genetic_flow/memory_pipeline/headless_orchestrator.py`

- **class `HeadlessOrchestrator`**
  - methods: `handle_input`

### `web/genetic_flow/memory_pipeline/rag_interceptor.py`

- **class `SimpleEmbedder`** — Computes fixed-dimension semantic vector via hashing.
  - methods: `embed`
- **class `RAGInterceptor`**
  - methods: `pre_flight_query`, `log_event`

### `web/genetic_flow/pyramid/code_sprite.py`

- **class `CodeSprite`** — Autonomous Dependency Sprite: Scans for imports and manifests environment.
  - methods: `_get_installed_packages`, `scan_and_fix`

### `web/genetic_flow/runtime_loop.py`

- `main_loop(max_gen)`

### `web/genetic_flow/symbolic_brain/engine.py`

- **class `SymbolicContextEngine`** — [PERFORMATIVE: TOKENIZE] Compiles dynamic AST tree; extracts parent/child shapes.
  - methods: `get_structural_signature`, `_walk_signature`, `generate_context_hash`, `update_relational_matrix`
- **class `ProductionRuleMatcher`** — [PERFORMATIVE: MATCH] Inductive Logic Loop matching pattern variations.
  - methods: `match_rule`
- **class `MutationInjector`** — [PERFORMATIVE: INJECT] Executes physical AST block mutations.
  - methods: `apply_mutation`
- **class `WeightBackpropagator`** — [PERFORMATIVE: UPDATE] Symbolic Backprop Step.
  - methods: `backprop`

### `web/genetic_flow/symbolic_brain/extractor.py`

- **class `SymbolicExtractor`** — Extracts symbolic rules from successful mutations in the ledger.
  - methods: `analyze_patterns`

### `web/genetic_flow/symbolic_brain/parser.py`

- **class `SymbolicParser`** — [PERFORMATIVE: TOKENIZE] Compiles live files into structured AST nodes.
  - methods: `get_signature_hash`, `_get_structural_string`, `map_token_relations`

### `web/genetic_flow/symbolic_brain/symbolic_inference.py`

- **class `SymbolicInference`** — [PERFORMATIVE: INFER] Selects target execution transformation rules.
  - methods: `infer_optimization_directive`

### `web/genetic_flow/symbolic_brain/weight_backprop.py`

- **class `WeightBackprop`** — [PERFORMATIVE: UPDATE] Calculates code fitness improvements and updates rule weights.
  - methods: `update_rule_weights`

### `web/genetic_flow/tracking_db/writer.py`

- `get_git_hash()`
- `store_mutation(chash, gen, score, code, task, ast_depth, stagnation, latency_delta)`

### `web/openrouter_cats_30/core/advanced_crawler.py`

- **class `Crawler`**
  - methods: `crawl`, `save_facts`

### `web/openrouter_cats_30/core/benchmark.py`

- `db_benchmark(db_url, num_queries, query_string)`
- `main()`

### `web/openrouter_cats_30/models/openrouter.py`

- **class `OpenRouterModel`**
  - methods: `process`

### `web/src/bridge.py`

- `desktop_sync()`

### `web/src/caching.py`

- `cache_get(h)`

### `web/src/diagnostic.py`

- `auto_fix(error)`

### `web/src/swarm.py`

- **class `SwarmAgent`**

### `web/tests/conftest.py`

- `client()`

### `web/tests/test_api.py`

- `test_api_get(client)`
- `test_api_post(client)`

## Public API index

| Module | Function | Signature |
|--------|----------|-----------|
| `AGENT_LAYER` | `auto_configure` | `auto_configure(intent)` |
| `FINAL_TEST_PILOT` | `test_no_refusal` | `test_no_refusal()` |
| `PEDAGOGY_HARVESTER` | `harvest` | `harvest()` |
| `PEDAGOGY_TRAINER` | `train_pattern` | `train_pattern(task, correct_command)` |
| `SCIENTIFIC_EXECUTOR` | `execute_step` | `execute_step(step_num, step_desc)` |
| `SCIENTIFIC_EXECUTOR` | `get_next_step` | `get_next_step()` |
| `SCIENTIFIC_EXECUTOR` | `log_scientific_step` | `log_scientific_step(step_num, step_desc, observation, hypothesis, experiment, result)` |
| `SCIENTIFIC_EXECUTOR` | `mark_step_complete` | `mark_step_complete(step_num)` |
| `SCIENTIFIC_EXECUTOR` | `run_with_limits` | `run_with_limits(command)` |
| `SEED_VAULT` | `seed_vault` | `seed_vault()` |
| `SubstrateOrganizer` | `organize_and_tidy` | `organize_and_tidy()` |
| `TODO_SCANNER` | `cleanup_completed` | `cleanup_completed()` |
| `TODO_SCANNER` | `scan_todos` | `scan_todos()` |
| `TODO_SCANNER` | `update_syphon` | `update_syphon(all_todos)` |
| `TODO_SYPHON` | `extract_from_chats` | `extract_from_chats()` |
| `TODO_SYPHON` | `update_syphon` | `update_syphon(new_todos)` |
| `Triton_Danube_Bridge` | `triton_execute` | `triton_execute(performative, payload)` |
| `Triton_Danube_Bridge` | `write_with_genetic_buffer` | `write_with_genetic_buffer(file_path, content)` |
| `action_recorder` | `record_action` | `record_action(performative, success)` |
| `action_sequencer` | `process_queue` | `process_queue()` |
| `agentic_sync_daemon` | `log` | `log(msg)` |
| `agentic_sync_daemon` | `main` | `main()` |
| `agentic_sync_daemon` | `run_sync_cycle` | `run_sync_cycle()` |
| `agy_python` | `call_openrouter` | `call_openrouter(prompt)` |
| `agy_python` | `get_openrouter_config` | `get_openrouter_config()` |
| `agy_python` | `log_interaction` | `log_interaction(prompt, response)` |
| `agy_python` | `main` | `main()` |
| `anti_hang_watchdog` | `execute_with_watchdog` | `execute_with_watchdog(func)` |
| `anti_hang_watchdog` | `trigger_failover` | `trigger_failover()` |
| `app` | `authenticate` | `authenticate(phrase)` |
| `app` | `establish_pipe` | `establish_pipe(ip, port, proto, auth_phrase)` |
| `app` | `get_telemetry` | `get_telemetry()` |
| `app` | `save_note` | `save_note(note_content, auth_phrase)` |
| `autonomous_engine` | `run_automated_tasks` | `run_automated_tasks()` |
| `autonomous_master` | `filter_and_route` | `filter_and_route(text)` |
| `autonomous_master` | `run_loop` | `run_loop()` |
| `autonomous_training_loop` | `training_cycle` | `training_cycle()` |
| `benchmark` | `db_benchmark` | `db_benchmark(db_url, num_queries, query_string)` |
| `benchmark` | `main` | `main()` |
| `bridge` | `desktop_sync` | `desktop_sync()` |
| `burn_in_tester` | `generate_noise` | `generate_noise(length)` |
| `burn_in_tester` | `run_burn_in` | `run_burn_in()` |
| `caching` | `cache_get` | `cache_get(h)` |
| `chat_harvester` | `extract_todos` | `extract_todos()` |
| `chat_template_pedagogy` | `learn_from_chats` | `learn_from_chats()` |
| `cognitive_db` | `init_db` | `init_db()` |
| `complete_roadmap` | `complete_roadmap` | `complete_roadmap(file_path)` |
| `conflict_resolver` | `resolve_conflict` | `resolve_conflict(local_state, remote_state)` |
| `conftest` | `client` | `client()` |
| `daemon` | `background_sync` | `background_sync()` |
| `daemon` | `run_ide` | `run_ide()` |
| `data_pipeline` | `data_preprocessing` | `data_preprocessing(df)` |
| `data_pipeline` | `model_training` | `model_training(df)` |
| `data_pipeline` | `pipeline` | `pipeline(df)` |
| `data_scraper` | `scrape_news_sources` | `scrape_news_sources()` |
| `db_analysis` | `analyze_schema` | `analyze_schema(db_name)` |
| `diagnostic` | `auto_fix` | `auto_fix(error)` |
| `download_weights` | `download_model` | `download_model()` |
| `enex_importer` | `import_enex` | `import_enex(enex_file_path)` |
| `engine_loop` | `extract` | `extract(text)` |

## Status

- Branch: `master`
- Last commit: 2026-06-27 09:18:36 -0600
- File types: .md ×153, .json ×32, .sh ×29, .txt ×28, .html ×20, .log ×10, .js ×9, .rs ×7

### Recent commits
```
fdef0d0 [Moe autonomous] MatrixCE_GUI 2026-06-27 09:18
1eb1034 [Moe autonomous] MatrixCE_GUI 2026-06-26 14:24
a8f82d9 [Moe autonomous] MatrixCE_GUI 2026-06-20 17:35
e8e49cf [Moe autonomous] MatrixCE_GUI 2026-06-20 09:18
5fdd56c [Moe autonomous] MatrixCE_GUI 2026-06-20 08:41
50fbaf5 [Moe autonomous] MatrixCE_GUI 2026-06-20 07:58
088e3b3 [Moe autonomous] MatrixCE_GUI 2026-06-20 07:20
05f1d22 [Moe autonomous] MatrixCE_GUI 2026-06-20 06:48
```

---
*README generated by `readme_generator.py` (Viper). Deterministic — derived from source, not LLM prose.*