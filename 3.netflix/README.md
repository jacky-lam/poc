In Netflix Dispatch, each domain folder typically contains at least:

- `models.py`: SQLAlchemy model definitions (including relationships).
- `service.py`: CRUD operations and some domain-logic that specifically pertains to that entity. Often includes repository-like functions or “services” for each model.
- `flows.py` (or sometimes called “workflow”): Larger orchestration that spans multiple services or triggers other domain actions.
- `plugins.py`: Integration points with Slack, email, or other external systems.

You’ll also see a global `database.py` or `config.py` that sets up the engine, session, configuration, etc.

## Domain-Focused Folders

Each domain (on_road_experiments, run_assignments, model_training_sessions, etc.) has a subfolder with models.py, service.py, (maybe) flows.py, plugins.py.

## Flows (Workflows)

“Flows” handle complex or multi-step processes that can cross domain boundaries. They may call multiple service layers, handle events or notifications, etc.

## Services

“Service” modules handle direct business logic, especially DB operations around your models. They typically revolve around standard CRUD plus domain-specific methods (like “mark assignment complete” or “mark experiment complete”).

## Plugins

Netflix Dispatch uses “plugins” to integrate with external services (Slack, email, etc.). For your domain, you might have a plugin to notify an external system that an experiment is done or to push metrics to a logging platform.

## Controllers / Routers

The actual HTTP endpoints (in a Flask or FastAPI sense) are typically minimal: they parse the request, call a flow or service, and then return a response.

## Note:

This approach is conceptually similar to the “MVC + Service” style, but with a strong emphasis on domain-based folder grouping and “flows” for orchestration, which you’ll see in Netflix’s Dispatch code base.
