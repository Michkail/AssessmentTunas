# - Arc _Odoo_
## uv _Package Manager_
### installation
> Windows
> $```powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"```

> Unix-based
> $```curl -LsSf https://astral.sh/uv/install.sh | sh```

### sync project dependencies
> $```uv sync```

### Odoo Environment
#### clone odoo repo
> $ ```git clone https://github.com/odoo/odoo.git --branch 14.0 --single-branch```

#### create custom_addons in odoo folder
> $ ```cd odoo```
```bash
custom_addons
├── pemesanan_ruangan/
│   ├── __init__.py
│   ├── __manifest__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── master_ruangan.py
│   │   └── pemesanan_ruangan.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── pemesanan_api.py
│   ├── views/
│   │   ├── master_ruangan_views.xml
│   │   ├── pemesanan_ruangan_views.xml
│   └── security/
│       ├── ir.model.access.csv
│       └── pemesanan_security.xml
```

### create odoo.conf in odoo folder or outer folder custom_addons
```
[options]
   addons_path = custom_addons,odoo/addons
   db_host = 127.0.0.1
   db_port = 5432
   db_user = odoo
   db_password = odoo
   logfile = odoo.log
   db_name = odoo14
```

# Run odoo
### normally or basic execution
> $ uv run odoo/odoo-bin

### advanced execution or with limits
> $ uv run odoo/odoo-bin --limit-memory-hard=0 --limit-memory-soft=0

_if found 0 error, program can access in *127.0.0.1:8069*_

# - Arc _expert_level.py_ Explanations
## file execution
> ```uv run python expert_level.py```
or
> ```uv run ./expert_level.py```

## input tests
### change this value conditionally
###### e.g.
```python
N = 5
M = 9
Ai = [2, 3, 6, 7, 8]
Bi = [3, 4, 2, 2, 3]
```

###### or
```python
N = 5
M = 3
Ai = [8, 4, 5, 6, 7]
Bi = [9, 8, 7, 5, 6]
```

###### or
```python
N = 4
M = 2
Ai = [8, 9, 3, 2]
Bi = [5, 4, 1, 3]
```
