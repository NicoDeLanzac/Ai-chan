FROM python:3.11-slim
WORKDIR /app
COPY Discord_Bot.py
RUN pip install --no-cache-dir discord.py
ENV DISCORD_TOKEN="your_token_here"
CMD ["python", "Discord_Bot.py"]
