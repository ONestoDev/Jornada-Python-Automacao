import json
from urllib.error import URLError
from urllib.request import Request, urlopen

import streamlit as st

st.set_page_config(
    page_title="Jarvis ChatBot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

NOME_MODELO = "qwen2.5:1.5b"


def conversar_com_modelo(mensagens):
    dados = json.dumps(
        {"model": NOME_MODELO, "messages": mensagens, "stream": False}
    ).encode("utf-8")
    requisicao = Request(
        "http://localhost:11434/api/chat",
        data=dados,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(requisicao, timeout=120) as resposta:
        return json.loads(resposta.read().decode("utf-8"))["message"]["content"]


st.sidebar.success("IA local gratuita — nenhuma chave de API necessária.")
st.sidebar.caption(f"Modelo: {NOME_MODELO}")

st.markdown(
    """
    <style>
    :root {
        --verde: #10B981;
        --verde-claro: #34D399;
        --roxo: #7C3AED;
        --roxo-claro: #A78BFA;
        --fundo: #0F0B1F;
        --fundo-2: #1A1130;
        --texto: #F5F3FF;
        --texto-suave: #C4B5FD;
    }

    .stApp {
        background: radial-gradient(circle at 20% 20%, rgba(124, 58, 237, 0.25), transparent 40%),
                    radial-gradient(circle at 80% 80%, rgba(16, 185, 129, 0.20), transparent 45%),
                    linear-gradient(135deg, #0F0B1F 0%, #1A1130 100%);
        color: var(--texto);
    }

    #MainMenu, footer {visibility: hidden;}

    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 8rem;
        max-width: 820px;
    }

    .titulo-container {
        text-align: center;
        margin-bottom: 2rem;
        padding: 1.8rem 1rem;
        background: linear-gradient(135deg, rgba(124, 58, 237, 0.18), rgba(16, 185, 129, 0.15));
        border: 1px solid rgba(167, 139, 250, 0.25);
        border-radius: 20px;
        backdrop-filter: blur(10px);
    }

    .titulo-container h1 {
        font-size: 2.6rem;
        font-weight: 800;
        margin: 0;
        background: linear-gradient(90deg, #34D399, #A78BFA, #7C3AED);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.5px;
    }

    .titulo-container p {
        color: var(--texto-suave);
        margin: 0.5rem 0 0 0;
        font-size: 0.98rem;
        opacity: 0.85;
    }

    .status-online {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 0.8rem;
        color: var(--verde-claro);
        margin-top: 0.7rem;
        padding: 0.3rem 0.8rem;
        border-radius: 999px;
        background: rgba(52, 211, 153, 0.12);
        border: 1px solid rgba(52, 211, 153, 0.3);
    }

    .status-online::before {
        content: "";
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: var(--verde-claro);
        box-shadow: 0 0 10px var(--verde-claro);
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.4; }
    }

    [data-testid="stChatMessage"] {
        background: transparent !important;
        border: none !important;
        padding: 0.4rem 0 !important;
    }

    [data-testid="stChatMessageContent"] {
        border-radius: 18px !important;
        padding: 0.9rem 1.2rem !important;
        font-size: 0.98rem;
        line-height: 1.55;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }

    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] {
        background: linear-gradient(135deg, #7C3AED 0%, #6D28D9 100%) !important;
        color: #ffffff !important;
        border: 1px solid rgba(167, 139, 250, 0.4);
    }

    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) [data-testid="stChatMessageContent"] {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.20) 0%, rgba(52, 211, 153, 0.10) 100%) !important;
        color: var(--texto) !important;
        border: 1px solid rgba(52, 211, 153, 0.35);
    }

    [data-testid="stChatMessageAvatarUser"] {
        background: linear-gradient(135deg, #A78BFA, #7C3AED) !important;
        border: 2px solid rgba(167, 139, 250, 0.5);
        box-shadow: 0 0 15px rgba(124, 58, 237, 0.5);
    }

    [data-testid="stChatMessageAvatarAssistant"] {
        background: linear-gradient(135deg, #34D399, #10B981) !important;
        border: 2px solid rgba(52, 211, 153, 0.5);
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.5);
    }

    [data-testid="stChatInput"] {
        background: rgba(26, 17, 48, 0.85) !important;
        border: 1px solid rgba(167, 139, 250, 0.3) !important;
        border-radius: 16px !important;
        backdrop-filter: blur(15px);
        box-shadow: 0 8px 30px rgba(124, 58, 237, 0.25);
    }

    [data-testid="stChatInput"] textarea,
    [data-testid="stChatInput"] input,
    [data-testid="stChatInput"] [contenteditable="true"] {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        caret-color: #000000 !important;
        font-size: 1rem !important;
        opacity: 1 !important;
    }

    [data-testid="stChatInput"] textarea::placeholder,
    [data-testid="stChatInput"] input::placeholder {
        color: #5F6368 !important;
        -webkit-text-fill-color: #5F6368 !important;
        opacity: 0.75 !important;
    }

    [data-testid="stChatInput"] button {
        background: linear-gradient(135deg, #10B981, #7C3AED) !important;
        border-radius: 12px !important;
        transition: transform 0.2s ease;
    }

    [data-testid="stChatInput"] button:hover {
        transform: scale(1.05);
    }

    .empty-state {
        text-align: center;
        padding: 3rem 1rem;
        color: var(--texto-suave);
        opacity: 0.75;
    }

    .empty-state .emoji {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        display: block;
    }

    .empty-state h3 {
        color: var(--texto);
        font-weight: 600;
        margin-bottom: 0.4rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="titulo-container">
        <h1>🤖 Jarvis ChatBot</h1>
        <p>Seu assistente inteligente com IA em tempo real</p>
        <div class="status-online">Online</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

if len(st.session_state["lista_mensagens"]) == 0:
    st.markdown(
        """
        <div class="empty-state">
            <span class="emoji">💬</span>
            <h3>Comece uma conversa</h3>
            <p>Envie uma mensagem para começar a interagir com a IA</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui...")

if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    try:
        with st.spinner("Pensando localmente..."):
            resposta_ia = conversar_com_modelo(st.session_state["lista_mensagens"])
        with st.chat_message("assistant"):
            st.write(resposta_ia)
        mensagem_ia = {"role": "assistant", "content": resposta_ia}
        st.session_state["lista_mensagens"].append(mensagem_ia)
    except URLError:
        st.error("O Ollama não está em execução. Inicie-o e tente novamente.")
    except TimeoutError:
        st.error("O modelo demorou para responder. Tente novamente.")
