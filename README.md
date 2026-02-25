# Feedback EVERSE Services

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18772729.svg)](https://doi.org/10.5281/zenodo.18772729)

Welcome to the central feedback repository for the **EVERSE (European Virtual Institute for Research Software Excellence)** tool suite. This space is dedicated to gathering insights, requirements, and technical reviews to ensure our tools meet the needs of the diverse research software community.

## 🛠 Our Services

We are currently collecting feedback for the following core components:

| Tool | Description | Service | Repository |
| --- | --- | --- | --- |
| **RSQKit** | Research Software Quality Toolkit | [View service](https://everse.software/RSQKit/) | [View Repo](https://github.com/EVERSE-ResearchSoftware/RSQKit) |
| **Quality Dimensions and Indicators** | List of Software Quality Dimensions and Indicators used in EVERSE | [View service](https://everse.software/indicators/website/indicators.html) | [View Repo](https://github.com/EVERSE-ResearchSoftware/indicators) |
| **TechRadar** | Visualizing the research software landscape | [View Service](https://everse.software/TechRadar/) | [View Repo](https://github.com/EVERSE-ResearchSoftware/TechRadar) |
| **QualityPipelines** | CI/CD templates for quality assurance | | [View Repo](https://github.com/EVERSE-ResearchSoftware/QualityPipelines) |
| **DashVERSE** | Analytics dashboard for the EVERSE ecosystem | | [View Repo](https://github.com/EVERSE-ResearchSoftware/DashVERSE) |
| ** EVERSE Training** | Educational resources for research software engineering | [View Service](https://everse-training.app.cern.ch/ ) | |

---

## 📥 How to Provide Feedback

We value input from both **users** (researchers, developers) and **domain experts** (community leads, RSE managers).

### 1. Structured Issues (Preferred)

Please use our [Issue Templates](https://github.com/EVERSE-ResearchSoftware/tools-feedback/issues) to ensure your feedback is routed correctly:

* **🐛 Bug Report:** Encountered a technical problem? Let us know.
* **💡 Feature Request:** Have a requirement for a new functionality?
* **🎓 Expert Community Review:** Deep-dive technical or domain-specific assessments.
* **💬 General Remarks:** Anything that doesn't fit the above.

### 2. Workshop & External Data

We collect feedback at the GAM and during dedicated sessions. To add the outcome of such feedback rounds to the repository

1. Navigate to the `/data` directory.
2. Open a Pull Request to upload your export (PDF, CSV, or Markdown summary).
3. Name your file or folder using the format: `YYYY-MM-DD-Workshop-Name` or similar.

Here, you can also add "random feedback" that does not fit the issue format.

---

## 📊 Feedback Organization

To keep the community informed on how their feedback is being used, we organize all input into a global dashboard:

👉 **Kanban board will follow**

We use labels to categorize feedback:

* `project:[tool-name]` — Which tool the feedback belongs to.
* `persona:expert` — Insights from community experts.
* `status:planned` — Feedback that has been accepted into the roadmap.
* `type:bug` — Type of issue as indicated above.

---

## 📜 License

This repository uses a **dual license** structure:

### Non-Code Contributions: CC-BY-4.0

All non-code contributions, including:
- Issues and bug reports
- Pull request descriptions and comments
- Documentation in the `/data` and `/docs` directories
- This README and other markdown documentation

Are licensed under [CC-BY-4.0](LICENSE).

### Code Contributions: MIT

All code contributions, including:
- Python scripts in `/scripts`
- CI/CD configurations
- Any executable code or automation scripts

Are licensed under the [MIT License](LICENSE-MIT).

By contributing to this project, you agree to license your contributions under the appropriate license based on the type of contribution.