FROM python:3.10
# Prepare installation env
RUN pip install pip==22.1
RUN pip install poetry
RUN poetry config virtualenvs.create false
# Copy app requirements and set workdir
COPY poetry.lock /app/
COPY pyproject.toml /app/
WORKDIR /app
# Install depenencies
RUN poetry install --no-root
# Copy root dir and instal library itself
COPY . /app/
RUN poetry install
# Expose port and setup healthcheck
EXPOSE 9000
HEALTHCHECK --timeout=3s --retries=2 --interval=60s CMD curl --fail http://localhost:9000/health || exit 1
# Start the app
RUN chmod +x deploy/start.sh
CMD ["/bin/bash", "-c", "deploy/start.sh"]
