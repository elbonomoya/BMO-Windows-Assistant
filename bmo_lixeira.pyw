import ctypes
import os

def mostrar_alerta(titulo, mensagem):
    # Mostra a caixa de diálogo clássica do Windows com estilo kawaii
    ctypes.windll.user32.MessageBoxW(0, mensagem, titulo, 0x40 | 0x1)

def esvaziar_lixeira():
    # Flags do Windows para esvaziar a lixeira sem mostrar confirmações estrondosas e sem som
    SHERB_NOCONFIRMATION = 0x00000001
    SHERB_NOPROGRESSUI       = 0x00000002
    SHERB_NOSOUND            = 0x00000004
    
    flags = SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND
    
    try:
        # Chama a API nativa do Windows para esvaziar a Recycle Bin
        resultado = ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, flags)
        
        if resultado == 0:
            mostrar_alerta(
                "BMO Recycle Bin! 🗑️✨", 
                "Lixeira limpa com sucesso! O BMO deu uma geral e deixou tudo tinindo e organizado! Bom trabalho! 🎮🧹"
            )
        else:
            mostrar_alerta(
                "BMO Recycle Bin! 🗑️", 
                "A lixeira já estava limpinha ou não há nada para apagar por agora! Tudo em ordem, chefe! 👍"
            )
    except Exception as e:
        mostrar_alerta("BMO Erro! ⚠️", f"Oops! Ocorreu um pequeno erro ao limpar: {str(e)}")

if __name__ == "__main__":
    esvaziar_lixeira()
