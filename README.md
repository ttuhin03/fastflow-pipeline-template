# 🚀 Fast-Flow Pipeline Template

Welcome to the official template for [Fast-Flow](https://github.com/ttuhin03/fastflow). This repository is designed to help you jumpstart your data workflows with a structure that is optimized for speed, reliability, and developer experience.

---

## 🏗️ How to Add a Pipeline

Fast-Flow is built on the principle of **Zero-Config Discovery**. You don't need to register pipelines in a database or a UI—just push your code.

1.  **Create a Directory**: Add a new folder under `pipelines/` (e.g., `pipelines/data_sync/`).
2.  **Add `main.py`**: This is your entry point. Fast-Flow will execute this file.
3.  **Define Dependencies**: Add a `requirements.txt` if you need external packages.
4.  **Configure (Optional)**: Add a `pipeline.json` to fine-tune resource limits and retries.

---

## 🧪 Local Testing: The "If it runs, it runs" Promise

The biggest pain point in modern orchestration is "Docker Hell"—where code works locally but fails in production due to environment mismatches.

**Fast-Flow eliminates this.** Because we use `uv` and a standardized runtime environment, local execution is identical to production execution.

### Test it in seconds:
```bash
cd pipelines/pipeline_a
pip install -r requirements.txt  # Or 'uv pip install' for speed
python main.py
```
> [!IMPORTANT]
> If your script runs successfully here, it is guaranteed to run in the Fast-Flow Orchestrator. No Docker image builds required.

---

## ⚡ The JIT (Just-In-Time) Effect

Fast-Flow doesn't use static Docker images for every pipeline. Instead, it uses a high-performance **JIT Containerization** approach:

-   **Instant Deployment**: Skip the 5-minute `docker build` and `docker push` cycle. Your code is live the moment you push to Git.
-   **UV Magic**: We use [uv](https://github.com/astral-sh/uv) to install dependencies at runtime.
-   **Aggressive Caching**: Thanks to a project-wide shared cache, dependency installation usually takes **< 500ms**.
-   **Isolation**: Every run still happens in a clean, isolated Docker container for security and resource control.

---

## 📂 Example Gallery

This template includes several pre-configured pipelines to demonstrate various scenarios:

| Pipeline | Purpose | Key Feature |
| :--- | :--- | :--- |
| `pipeline_a` | **Standard Example** | Env vars + `requirements.txt` |
| `pipeline_b` | **Custom Metadata** | Uses `data_processor.json` instead of `pipeline.json` |
| `pipeline_c` | **Minimalist** | Only a `main.py`—nothing else |
| `failing_pipeline` | **Error Testing** | Demonstrates how failures look in the UI |
| `delayed_success` | **Runtime Testing** | 20s delay to test status monitoring |
| `delayed_random` | **Retry Demo** | 20s delay followed by random success/failure |
| `ram_limit_fail` | **OOM Safety** | Consumes 100MB with a 50MB limit (Should fail) |
| `ram_limit_success`| **Resource Control** | Consumes 100MB with a 256MB limit (Should pass) |

---

## 🛠️ Configuration Reference (`pipeline.json`)

Fine-tune your pipelines by adding a `pipeline.json` file in the pipeline directory.

### 💾 Resource Limits
| Field | Default | Description |
| :--- | :--- | :--- |
| `cpu_hard_limit` | None | Max CPU cores (e.g., `0.5`, `2.0`). Strictly enforced. |
| `mem_hard_limit` | None | Max RAM (e.g., `"512m"`, `"2g"`). Triggers OOM-kill if exceeded. |
| `cpu_soft_limit` | None | Threshold for UI warnings/monitoring. |
| `mem_soft_limit` | None | Threshold for UI warnings/monitoring. |

### 🔄 Retries & Error Handling
We support advanced retry strategies out of the box:

-   **Exponential Backoff**: Ideal for flaky third-party APIs.
-   **Fixed Delay**: Good for internal services that need a quick breather.
-   **Custom Schedule**: For when you need specific timing (e.g., `[60, 300, 3600]`).

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

### 🔗 Triggering via Webhooks
You can trigger any pipeline via a simple HTTP POST request if you define a `webhook_key`:

```json
{ "webhook_key": "your-secret-key" }
```
**Endpoint**: `POST /api/webhooks/{pipeline_id}/{webhook_key}`

---

## 🌟 Best Practices

1.  **Clean Code**: Keep your `main.py` modular. Feel free to add sub-modules in the same folder.
2.  **Environment Variables**: Use `os.getenv()` for configuration. Secure secrets are managed in the Fast-Flow UI.
3.  **Logs**: Just use `print()`. Fast-Flow captures stdout and stderr automatically and streams them to the UI.