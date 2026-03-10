import os

# Define a ordem dos componentes para montar o index.html
components = [
    'src/layout/head.html',
    'src/layout/styles.html',
    'src/layout/scripts_tracking.html',
    'src/layout/back_redirect.html',
    'src/layout/popup.html',
    'src/layout/header.html',
    'src/layout/video_section.html',
    'src/layout/tracking_events.html',
    'src/layout/footer.html'
]

def build():
    print("Iniciando construção do index.html...")
    content = ""
    
    for component in components:
        if os.path.exists(component):
            with open(component, 'r', encoding='utf-8') as f:
                content += f.read() + "\n"
                print(f"  [+] Adicionado: {component}")
        else:
            print(f"  [!] Alerta: Componente não encontrado: {component}")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content.strip())
    
    print("-----------------------------------")
    print("Sucesso! index.html foi gerado na raiz.")

if __name__ == "__main__":
    build()
