# Mackerel API Client for Python

## TL;DR

- `makapi.py` Mackerel API をPythonから叩くための自家製モジュール
    - Mackerel APIについては https://mackerel.io/ja/api-docs/ を参照のこと
- `pakapi` 上記モジュールを使って、CLIからMackerel APIを叩くためのコマンド

## USAGE

### makapi.py

```python
from makapi import makapi

m = makapi(MACKEREL_APIKEY)

m.get('org')
m.put('hosts/<hostId>')
m.post('hosts/<hostId>/status','{"status":"standby"}')
m.delete('services/<serviceName>')
```

### pakapi

```
Usage: pakapi METHOD API { payload }

  METHOD ... get / put / post / delete
  API ...... '/api/v0/' is not need. See https://mackerel.io/ja/api-docs/
  payload .. specify Input as JSON format

Example: pakapi get org
         pakapi post hosts/<hostId>/status '{"status":"standby"}'
         pakapi help
```

