# Fast-Flow Pipeline Template

Welcome to the official template for [Fast-Flow](https://github.com/ttuhin03/fastflow) pipelines. This repository serves as a blueprint for structuring your data pipelines and configuring them for the Fast-Flow Orchestrator.

## How to add a pipeline

Adding a new pipeline is as simple as creating a folder. Fast-Flow uses **Automatic Discovery**, so there's no need for manual registration.

1. **Create a folder** under `pipelines/` (e.g., `pipelines/my_new_pipeline/`). The folder name will be the pipeline's name.
2. **Add a `main.py`**: This is the only required file. It contains your pipeline logic.
3. **(Optional) Add `requirements.txt`**: List any Python dependencies your script needs.
4. **(Optional) Add `pipeline.json`**: Define resource limits, retries, and other metadata.

---

## Local Testing

One of the key advantages of Fast-Flow is that **if it runs locally, it runs in the Orchestrator.** You don't need to build Docker images or manage complex environments.

### The `uv` Advantage
Fast-Flow uses `uv` under the hood for blazing-fast execution and dependency management. To test your pipeline locally:

```bash
cd pipelines/pipeline_a
pip install -r requirements.txt  # Or use 'uv pip install'
python main.py
```

**If this works on your machine, it will work exactly the same way in the Fast-Flow Orchestrator.**

---

## The JIT Effect

Forget about slow Docker builds and registry pushes. Fast-Flow uses a **Just-In-Time (JIT)** approach to containerization:

- **No Docker Builds**: Your code is synced via Git and executed immediately.
- **UV-Cache Magic**: Dependencies are installed on-the-fly via `uv`. 
- **Lightning Fast**: Thanks to a shared cache, dependency installation usually takes **less than 1 second** for cached items.
- **Pre-Heat**: The system can even "pre-heat" your dependencies during the Git sync, so they are ready before the first run.

---

## Pipeline Repository Documentation

### Directory Structure

```text
pipelines/
├── pipeline_a/
│   ├── main.py              # Required
│   ├── requirements.txt     # Optional
│   └── pipeline.json        # Optional metadata
├── pipeline_b/
│   ├── main.py
│   └── data_processor.json  # Alternative: {pipeline_name}.json
├── pipeline_c/
│   └── main.py              # Minimal setup
├── failing_pipeline/
│   └── main.py              # Always fails (testing)
├── ram_limit_fail/
│   ├── main.py              # Consumes 100MB, 50MB limit
│   └── pipeline.json
├── ram_limit_success/
│   ├── main.py              # Consumes 100MB, 256MB limit
│   └── pipeline.json
└── delayed_random/
    └── main.py              # 20s delay, random outcome
```

### Pipeline Detection
- **Discovery**: Automatically detected via Git sync.
- **Validation**: Must contain a `main.py`.
- **Naming**: Folder name = Pipeline ID.

---

## Configuration Reference (`pipeline.json`)

All fields in `pipeline.json` (or `{pipeline_name}.json`) are optional.

### Resource Limits
| Field | Type | Description |
| :--- | :--- | :--- |
| `cpu_hard_limit` | Float | CPU cores (e.g., `1.0`, `0.5`). Enforced by Docker. |
| `mem_hard_limit` | String| RAM limit (e.g., `"512m"`, `"1g"`). Triggers OOM-kill if exceeded. |
| `cpu_soft_limit` | Float | Monitoring threshold for CPU. |
| `mem_soft_limit` | String| Monitoring threshold for Memory. |

### Scheduler & Retries
| Field | Type | Description |
| :--- | :--- | :--- |
| `timeout` | Int | Max runtime in seconds before the run is aborted. |
| `retry_attempts`| Int | Number of retry attempts on failure. |
| `enabled` | Bool | Whether the pipeline is active (`true` by default). |

### Retry Strategy Examples

**Exponential Backoff** (Best for external APIs):
```json
{
  "retry_attempts": 3,
  "retry_strategy": {
    "type": "exponential_backoff",
    "initial_delay": 60,
    "max_delay": 3600,
    "multiplier": 2.0
  }
}
```

**Fixed Delay** (Best for internal services):
```json
{
  "retry_attempts": 3,
  "retry_strategy": {
    "type": "fixed_delay",
    "delay": 120
  }
}
```

### Webhooks & Environment
- **`default_env`**: Set default environment variables for your pipeline. (Note: Use the UI for Secrets!)
- **`webhook_key`**: A secret key to trigger your pipeline via HTTP POST:
  `POST /api/webhooks/{pipeline_name}/{webhook_key}`

---

## Best Practices
1. **Pin Dependencies**: Use specific versions in `requirements.txt`.
2. **Secrets**: Never commit secrets to the repo. Use the Fast-Flow UI's secret management.
3. **Descriptions**: Add a `description` in your JSON for better UI visibility.