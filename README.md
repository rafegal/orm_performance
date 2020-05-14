# Django ORM Performance

Este projeto está relacionado ao conteúdo explicado no meu canal do Youtube, para melhor entendimento acesse:

Projeto para demonstrar a diferença de performance entre uma consulta simples e uma consulta com select_related (join) quando uma FK for utilizada e campos especificados, evitando retornar dado desnecessário do banco de dados.

sqlite3 já carregado e com informações para testes.

```
pip install -r requirements.txt
```

```
python manage.py runserver
```

## Testes

https://127.0.0.1/vendas/

![](images/readme/vendas.png)

https://127.0.0.1/vendas/performance

![](images/readme/vendas_performance.png)

Admin User: admin  
Admin Password: admin123