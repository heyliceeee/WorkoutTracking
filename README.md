# 🏋️‍♀️ Workout Tracking Automation

Este projeto automatiza o registo de treinos num Google Sheet, permitindo acompanhar exercícios, duração e calorias queimadas de forma simples e centralizada.

A aplicação integra duas APIs:

- **Nutrition API** — interpreta descrições de exercícios e calcula calorias queimadas com base em peso, altura, idade e género.  
- **Sheety API** — regista automaticamente cada treino numa folha de cálculo, organizada com as colunas `date`, `time`, `exercise`, `duration` e `calories`.

O fluxo é totalmente automatizado: o utilizador descreve o exercício realizado, os dados são processados e o registo é imediatamente adicionado à folha.

---

## ✨ Funcionalidades

- Processamento automático de descrições como *“walked 6 miles”* ou *“ran 20 minutes”*.  
- Cálculo de calorias com base em dados pessoais.  
- Registo estruturado de cada treino num Google Sheet.  
- Histórico acessível e organizado para análise e acompanhamento.  
- Integração transparente entre APIs externas.

---

## 📊 Estrutura do registo

Cada entrada contém:

- **date** — data do treino  
- **time** — hora do registo  
- **exercise** — nome do exercício interpretado  
- **duration** — duração em minutos  
- **calories** — calorias queimadas estimadas  

---

## 🎯 Objetivo

Simplificar o acompanhamento de treinos, eliminando registos manuais e garantindo dados consistentes e centralizados para análise de progresso.