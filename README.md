# AutOps 🤖

> **Autonomous server monitoring & self-healing platform powered by AI** — detects anomalies, diagnoses issues via RAG-based knowledge retrieval, and executes approved remediations over SSH, with human-in-the-loop safety gates and Discord-based remote control.

---

## ✨ Features

- **Real-time Monitoring** — Continuously tracks server health: CPU, memory, disk, and services
- **AI-Powered Diagnostics** — Uses RAG (Retrieval-Augmented Generation) with a Pinecone vector database to intelligently diagnose issues
- **Autonomous Remediation** — Executes fixes over SSH based on AI recommendations
- **Human-in-the-Loop** — Critical actions require human approval before execution — no rogue fixes
- **Discord Control Panel** — Query server status, receive alerts, and approve/reject actions from your phone
- **Modular Architecture** — Fully Docker-based, decoupled components for easy scaling and maintenance

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                   Target Servers                    │
│           (Monitored via SSH & Agents)              │
└────────────────────┬────────────────────────────────┘
                     │ Metrics / Alerts
                     ▼
┌─────────────────────────────────────────────────────┐
│              n8n Automation Engine                  │
│         (Hosted on VPS · Nginx + SSL)               │
│              autops.online                          │
└───────┬─────────────────────────┬───────────────────┘
        │                         │
        ▼                         ▼
┌───────────────┐       ┌─────────────────────┐
│  AI Diagnosis │       │  RAG Knowledge Base  │
│  (LLM Layer)  │◄─────►│  (Pinecone Vector DB)│
└───────┬───────┘       └─────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────────┐
│             Discord Integration                   │
│   Alerts · Status Queries · Approval Gates        │
└───────────────────────────────────────────────────┘
        │ Human Approves
        ▼
┌───────────────────────────────────────────────────┐
│           SSH Remediation Executor                │
│        (Runs fixes on target servers)             │
└───────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Automation Engine | [n8n](https://n8n.io/) |
| AI / LLM | Claude (Anthropic) |
| Vector Database | Pinecone |
| Reverse Proxy | Nginx + SSL (Let's Encrypt) |
| Remote Execution | SSH |
| Control Interface | Discord Bot |
| Infrastructure | Docker (containerized, modular) |
| Hosting | VPS (autops.online) |

---

## 🚀 Getting Started

### Prerequisites

- Docker & Docker Compose
- A VPS with a public domain (e.g., `autops.online`)
- Discord Bot Token
- Pinecone API Key
- Anthropic API Key
- SSH access to target servers

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/autops.git
cd autops

# 2. Copy and configure environment variables
cp .env.example .env
# Edit .env with your API keys and configuration

# 3. Start the stack
docker compose up -d

# 4. Set up Nginx reverse proxy with SSL
# (See docs/nginx-setup.md for instructions)
```

### Configuration

Edit `.env` with your credentials:

```env
ANTHROPIC_API_KEY=your_key_here
PINECONE_API_KEY=your_key_here
DISCORD_BOT_TOKEN=your_token_here
SSH_PRIVATE_KEY_PATH=/path/to/key
N8N_WEBHOOK_URL=https://autops.online
```

---

## 🔒 Safety First

AutOps is built with safety as a core principle:

- **No autonomous critical actions** — any remediation that affects running services, restarts processes, or modifies configurations requires explicit human approval via Discord
- **Audit trail** — all actions, approvals, and rejections are logged
- **Fail-safe defaults** — if the AI is uncertain, it escalates to human review rather than guessing

---

## 📱 Discord Commands

| Command | Description |
|---|---|
| `/status` | Get current health overview of all servers |
| `/server <name>` | Detailed stats for a specific server |
| `/approve <id>` | Approve a pending remediation action |
| `/reject <id>` | Reject a pending remediation action |
| `/history` | View recent actions and remediations |

---

## 📁 Project Structure

```
autops/
├── docker-compose.yml
├── .env.example
├── nginx/
│   └── autops.conf
├── n8n/
│   └── workflows/
├── discord-bot/
├── knowledge-base/
│   └── (RAG documents & embeddings)
├── scripts/
│   └── ssh-executor/
└── docs/
    ├── architecture.md
    └── nginx-setup.md
```

---

## 📄 License

This project is licensed under the Apache 2.0 License — see the (LICENSE) file for details.

---

## 👨‍💻 Author

**Ali** — IT System Administrator & BS-IT Final Year Student  

---

> ⚠️ **Disclaimer:** AutOps is a Final Year Project (FYP) and is under active development. Use in production environments at your own discretion.
