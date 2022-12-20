FROM python:3.9.5

WORKDIR /Users/alexismoreno/gitrepos/US_Population

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
