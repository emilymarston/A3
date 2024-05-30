from flask import Blueprint, request, jsonify, abort

payment_routes = Blueprint('payment_method_routes', __name__)

@payment_routes.route('/payment/cash', methods=['POST'])
def pay_by_cash():
    data = request.json
    amount = data.get('amount')
    if amount is None:
        abort(400, description="Amount is required")
    
    payment_method = Cash()
    try:
        payment_method.process_payment(amount)
        return jsonify({"message": f"Payment of {amount:.2f} processed by {payment_method.get_payment_method()}"}), 200
    except Exception as e:
        abort(400, description=str(e))

@payment_routes.route('/payment/debit_card', methods=['POST'])
def pay_by_debit_card():
    data = request.json
    amount = data.get('amount')
    if amount is None:
        abort(400, description="Amount is required")
    
    payment_method = CreditCard()
    try:
        payment_method.process_payment(amount)
        return jsonify({"message": f"Payment of {amount:.2f} processed by {payment_method.get_payment_method()} with surcharge"}), 200
    except Exception as e:
        abort(400, description=str(e))
