from app.funcao import funcao_hello_world

def test_funcao_hello_world_deve_retornar_hello_world():
    response = funcao_hello_world()

    assert response == 'hello world'