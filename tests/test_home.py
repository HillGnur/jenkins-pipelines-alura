import time

def test_home(browser):
    url = "http://127.0.0.1:8090"

    browser.get(url)
    time.sleep(10)

    assert "Dashboard" in browser.title
    assert "pagina inicial" in browser.page_source
    print("Teste da página inicial realizado com sucesso!")
