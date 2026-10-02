# EOSC Service Catalogue — reference specification and sample implementation

This repository supports **Registration of EOSC Service Catalogues in the EOSC EU
Node**. A node that wants its service catalogue registered must expose an HTTP
endpoint the EU Node can harvest. This repository defines what that endpoint has
to look like, in two forms:

- **`service_catalogue.schema.json`** — the reference OpenAPI 3.1 specification.
  This is the contract: the request parameters, the response envelope, the
  service profile, and the controlled vocabularies.
- **`main.py`** + **`catalogue_model.py`** — a small, runnable sample
  implementation of that contract, serving mock data.

The sample is a working example, not a product. It is not meant to be deployed
as a node's catalogue; implement the contract in whatever stack you already use.

## Running the sample

```sh
pip install fastapi uvicorn
uvicorn main:app --reload
```

Then `http://127.0.0.1:8000/services?quantity=5`, with interactive docs at
`http://127.0.0.1:8000/docs`.

## Regenerating the specification

`service_catalogue.schema.json` is **generated from the sample implementation**
— `catalogue_model.py` holds the Pydantic models, and FastAPI derives the
OpenAPI document from them. Edit the models, never the JSON, then regenerate:

```sh
python -c 'import json; from main import app; \
  open("service_catalogue.schema.json","w").write(
      json.dumps(app.openapi(), indent=2, ensure_ascii=False))'
```

`ensure_ascii=False` and no trailing newline keep the output byte-identical to
the committed file, so the diff shows only real changes.

One Pydantic subtlety worth knowing when editing the models: `Optional[X]` does
**not** make a field optional on its own. Without a default it stays required —
present, though permitted to be null. A field that may be omitted needs
`Field(None, ...)`.
