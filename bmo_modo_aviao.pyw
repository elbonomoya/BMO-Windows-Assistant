import ctypes
import psutil
import time

def mostrar_alerta(titulo, mensagem):
    # Mostra uma caixa de diálogo limpa e kawaii do Windows
    ctypes.windll.user32.MessageBoxW(0, mensagem, titulo, 0x40 | 0x1)

def verificar_modo_aviao():
    # Verifica o estado das conexões de rede ativas
    stats = psutil.net_if_stats()
    
    # Se todas as principais interfaces de rede estiverem em baixo, 
    # o BMO assume que o Modo Avião foi ativado!
    interfaces_ativas = any(stat.isup for name, stat in stats.items() if not name.startswith('Loopback'))
    
    if not interfaces_ativas:
        mostrar_alerta(
            "BMO Airport Mode! ✈️🌍", 
            "Modo Avião detetado! Vais viajar, amigo? Boa viagem! Prepara os snacks e diverte-te muito! 🎒✨🎮"
        )

if __name__ == "__main__":
    verificar_modo_aviao()
