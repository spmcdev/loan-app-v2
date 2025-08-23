from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import date
import os
import uvicorn

app = FastAPI(title="Loan App API (Backend Only)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

loans = []
payments = []
loan_id_counter = 1
payment_id_counter = 1

# Health check endpoint
@app.get("/")
def root():
    return {"message": "Loan App API is running!", "status": "healthy", "version": "1.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "loans_count": len(loans), "payments_count": len(payments)}

# -------------------------
# Models
# -------------------------
class Loan(BaseModel):
    borrower_id: str   # <- new field
    borrower: str
    amount: float
    interest: float
    weeks: int
    start_date: date

class Payment(BaseModel):
    loan_id: int
    week: int
    amount: float

# -------------------------
# Loans Routes
# -------------------------
@app.get("/loans")
def get_loans():
    return loans

@app.post("/loans")
def add_loan(loan: Loan):
    global loan_id_counter
    loan_dict = loan.dict()
    loan_dict["id"] = loan_id_counter
    loan_id_counter += 1
    loans.append(loan_dict)
    return loan_dict

@app.delete("/loans/{loan_id}")
def delete_loan(loan_id: int):
    global loans, payments
    loan_exists = False
    for l in loans:
        if l["id"] == loan_id:
            loan_exists = True
            loans.remove(l)
            break
    if not loan_exists:
        raise HTTPException(status_code=404, detail="Loan not found")
    payments = [p for p in payments if p["loan_id"] != loan_id]
    return {"detail": f"Loan {loan_id} deleted"}

# -------------------------
# Payments Routes
# -------------------------
@app.get("/payments")
def get_payments():
    return payments

@app.post("/payments")
def add_payment(payment: Payment):
    global payment_id_counter
    payment_dict = payment.dict()
    payment_dict["id"] = payment_id_counter
    payment_id_counter += 1
    payments.append(payment_dict)
    return payment_dict

@app.delete("/payments/{payment_id}")
def delete_payment(payment_id: int):
    global payments
    for p in payments:
        if p["id"] == payment_id:
            payments.remove(p)
            return {"detail": f"Payment {payment_id} deleted"}
    raise HTTPException(status_code=404, detail="Payment not found")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
