import streamlit as st
from service.blob_service import upload_blob

def configure_interface():
  st.title("Upload de Arquvivo - Desafio 1 - azure - Fake Docs")
  uploaded_file = st.file_uploader(label="Escolha um arquivo", type=["png","jpg", "jpeg"])
  
  if uploaded_file is not None:
    fileName = uploaded_file.name
    try: 
      blob_url = upload_blob(uploaded_file, fileName)
      if blob_url:
        st.write(f"Arquivo {fileName} foi enviado para o Azure Blog Storage, com sucesso")
        try:
          credit_card_info = "" #chamar function cardcredit
          show_image_and_validation(blob_url, credit_card_info)
        except Exception as e:
          st.error(f"Error ao analisar o cartão {str(e)}")
      else:
        st.write(f"Erro ao enviar o arquivo {fileName} para o Azure Blob Storage")
    except Exception as e:
      st.error(f"Erro ao processar o arquivo {fileName}:{str(e)}")
  
def show_image_and_validation(blob_url, credit_card_info):
  st.image(blob_url, caption="Imagem enviada", use_container_width=True)
  st.write("Resultado da validação:")
  if credit_card_info and credit_card_info["card_name"]:
    st.markdown(f"<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
    st.write(f"Nome do Titular: {credit_card_info['card_name']}")
    st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
    st.write(f"Data de Validade: {credit_card_info['expiry_date']}")
  else:
    st.markdown(f"<h1 style='color: red;'>Cartão Invalido</h1>", unsafe_allow_html=True)
    st.write("este n e um cartão de credito valido")
  
if __name__ == "__main__":
  configure_interface()