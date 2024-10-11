# 🎟️ Tickets Analyzer API

Welcome to the **Tickets Analyzer API**! 🚀
This API allows you to upload ticket files in PDF and get normalized information about their items in JSON.

## 🛒 Supported supermarkets

- **[<span style="color:lightgreen;">Mercadona</span>](https://www.mercadona.es/)**

## 🚀 Getting Started

To get started with the **Tickets Analyzer API**, follow these steps:

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/csp33/tickets-analyzer-api.git
   ```
2. Start the API with Docker 🐳
   ```bash
   docker compose up --build
   ```
3. Enter [the Swagger documentation](http://0.0.0.0:8000/docs) and upload a ticket.

### Example response

```json
{
  "items": [
    {
      "quantity": 1,
      "description": "DUO CANONIGOS RUCULA",
      "unit_price": 1.38,
      "total_price": 1.38
    },
    {
      "quantity": 1,
      "description": "DIGEST",
      "unit_price": 1.05,
      "total_price": 1.05
    },
    {
      "quantity": 1,
      "description": "QUESO LONCHAS LIGHT",
      "unit_price": 2.26,
      "total_price": 2.26
    },
    {
      "quantity": 1,
      "description": "PATATA 3 KG",
      "unit_price": 5,
      "total_price": 5
    },
    {
      "quantity": 1,
      "description": "PIMIENTO CONGELADO",
      "unit_price": 1.25,
      "total_price": 1.25
    }
  ]
}
```
