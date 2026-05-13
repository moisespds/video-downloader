# 🚀 Internet Video Downloader

## 📌 Overview

Internet Video Downloader is a web application designed to download videos from the internet in a simple, secure, and ad-free way.

This project was created with a focus on **internal company usage**, allowing IT teams to provide a reliable tool for downloading media content without relying on unsafe or ad-heavy websites.

---

## 🎯 Problem

In corporate environments, downloading videos from the internet is often necessary for internal use (training, presentations, media servers, etc.).

However:

- Most free tools and websites are full of ads and misleading buttons
- Many of these websites are blocked by corporate firewalls
- There are security risks when using untrusted platforms
- The process is time-consuming, even for IT professionals

---

## 💡 Solution

This project provides a **self-hosted web application** that allows companies to:

- Download videos directly from a clean interface
- Avoid ads and malicious websites
- Maintain security within the corporate network
- Centralize media downloads through the IT team

It can be used in two ways:

1. **Local mode (quick use)** → run on a personal machine (localhost)
2. **Server mode (recommended)** → deploy on an internal server and share with employees

---

## 🏗️ Architecture

- **Backend:** Django (Python)
- **Download engine:** yt-dlp
- **Media processing:** FFmpeg

Architecture style:
- MVC (Model-View-Controller)
- Monolithic application

---

## ⚙️ Technologies

- Python
- Django
- yt-dlp
- FFmpeg

---

## ▶️ How to Run (Plug-and-Play)

### 1. Clone the repository

```bash
git clone https://github.com/moisespds/video-downloader
cd yt-downloader/core
2. Create virtual environment
python -m venv venv
3. Activate environment

Windows:

venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Run database migrations
python manage.py migrate
6. Install FFmpeg

Download from:
https://www.ffmpeg.org/download.html#build-windows

Verify installation:

ffmpeg -version
7. Start the server
python manage.py runserver

Or simply run:

start.bat
8. Access the system

Open your browser:

http://127.0.0.1:8000
🔧 Internal Server Deployment (Advanced)

For company usage:

Install Python on the server
Set up virtual environment
Install dependencies
Run the application
Configure network access (intranet)
(Optional) Run as a service
⚠️ Notes
FFmpeg is required for audio extraction
Recommended for internal/company use
Downloads are saved locally in the project folder
📈 Future Improvements
Authentication system (internal users)
Download history
Integration with file servers (NAS)
Improved UI/UX
Background processing (Celery)
📚 Learnings

This project helped me develop:

Backend development with Django
Integration with external tools (yt-dlp)
System design thinking for real-world problems
Git workflow (feature branches, PRs, code review)
Building solutions for corporate environments
🤝 Contributing

Contributions are welcome.

📄 License

MIT


---

# 🇧🇷 VERSÃO EM PORTUGUÊS (BRASIL)

```markdown
# 🚀 Internet Video Downloader

## 📌 Visão Geral

O Internet Video Downloader é uma aplicação web desenvolvida para realizar download de vídeos da internet de forma simples, segura e sem anúncios.

O projeto foi criado com foco em **uso interno em empresas**, permitindo que equipes de TI disponibilizem uma ferramenta confiável para download de mídias sem depender de sites inseguros.

---

## 🎯 Problema

Em ambientes corporativos, muitas vezes é necessário baixar vídeos da internet para uso interno (treinamentos, apresentações, servidores de mídia, etc.).

Porém:

- A maioria dos sites gratuitos possuem muitos anúncios e botões enganosos
- Esses sites geralmente são bloqueados por firewall corporativo
- Existem riscos de segurança ao utilizar plataformas desconhecidas
- O processo é demorado até mesmo para profissionais de TI

---

## 💡 Solução

Este projeto fornece uma **aplicação web interna** que permite:

- Baixar vídeos através de uma interface simples
- Evitar anúncios e sites maliciosos
- Garantir mais segurança dentro da rede da empresa
- Centralizar downloads na equipe de TI

Pode ser utilizado de duas formas:

1. **Modo local (rápido)** → rodando na própria máquina
2. **Modo servidor (recomendado)** → disponível na rede interna da empresa

---

## 🏗️ Arquitetura

- **Backend:** Django (Python)
- **Motor de download:** yt-dlp
- **Processamento de mídia:** FFmpeg

Arquitetura:
- MVC (Model-View-Controller)
- Aplicação monolítica

---

## ⚙️ Tecnologias

- Python
- Django
- yt-dlp
- FFmpeg

---

## ▶️ Como Executar (Plug-and-Play)

### 1. Clonar o repositório

```bash
git clone https://github.com/moisespds/video-downloader
cd yt-downloader/core
2. Criar ambiente virtual
python -m venv venv
3. Ativar ambiente
venv\Scripts\activate
4. Instalar dependências
pip install -r requirements.txt
5. Rodar migrações
python manage.py migrate
6. Instalar FFmpeg

Baixar em:
https://www.ffmpeg.org/download.html#build-windows

Verificar:

ffmpeg -version
7. Iniciar o servidor
python manage.py runserver

Ou:

start.bat
8. Acessar o sistema

Abrir no navegador:

http://127.0.0.1:8000
🔧 Uso em Servidor Interno

Para empresas:

Instalar Python no servidor
Criar ambiente virtual
Instalar dependências
Executar aplicação
Liberar acesso na rede interna
(Opcional) rodar como serviço
⚠️ Observações
FFmpeg é necessário para baixar áudio
Recomendado para uso interno
Arquivos são salvos localmente
📈 Melhorias Futuras
Sistema de autenticação
Histórico de downloads
Integração com servidores de arquivos (NAS)
Melhorias de interface
Processamento assíncrono
📚 Aprendizados

Este projeto me ajudou a desenvolver:

Backend com Django
Integração com ferramentas externas
Pensamento de solução para problemas reais
Uso profissional do Git
Criação de sistemas para ambiente corporativo
🤝 Contribuição

Contribuições são bem-vindas.

📄 Licença

MIT
