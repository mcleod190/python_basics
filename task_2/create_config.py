import yaml

struct = {
    'my_project': {
        'settings': {
            '__init__.py': None,
            'dev.py': None,
            'prod.py': None
        },
        'mainapp': {
            '__init__.py': None,
            'models.py': None,
            'views.py': None,
            'templates': {
                'mainapp': {
                    'base.html': None,
                    'index.html': None
                }
            }
        },
        'authapp': {
            '--__init__.py': None,
            'models.py': None,
            'views.py': None,
            'templates': {
                'authapp': {
                    'base.html': None,
                    'index.html': None
                }

            }
            
        }
    }
}

def create_config(struct):
    with open("config.yaml", 'w', encoding='utf8') as stream:
        yaml.dump(struct, stream, default_flow_style=False, allow_unicode=True,)

if __name__ == '__main__':
    create_config(struct)

