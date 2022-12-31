# Exercise to implement recursive functions in python and memoizing
import time
start_time = time.time()

TAXES = [{
    "tax_name": "iva",
    "value": 16,# Representation in percent
}, {
    "tax_name": "ieps",# Impuesto Especial sobre Producción y Servicios (IEPS)
    "value": 8,# Representation in percent
}, {
    "tax_name": "dta",# Derecho de Trámite Aduanero (DTA)
    "value": 2,# Representation in percent
}]
quotes_to_calculate = [{
    "user_id": 1,
    "products": [{
        "product_name": "laptop HP",
        "price_before_taxes": 10233.00,
    }, {
        "product_name": "magic mouse",
        "price_before_taxes": 102.00,
    }, {
        "product_name": "printer",
        "price_before_taxes": 1012.12,
    }, {
        "product_name": "smart watch",
        "price_before_taxes": 102.00,
    }]
}, {
    "user_id": 2,
    "products": [{
        "product_name": "laptop DELL",
        "price_before_taxes": 20119.79,
    }, {
        "product_name": "printer",
        "price_before_taxes": 1012.12,
    }, {
        "product_name": "smart watch",
        "price_before_taxes": 102.00,
    }, {
        "product_name": "web cam",
        "price_before_taxes": 99.98,
    }]
}, {
    "user_id": 3,
    "products": [{
        "product_name": "laptop MacBook Pro",
        "price_before_taxes": 49999.99,
    }, {
        "product_name": "magic mouse",
        "price_before_taxes": 102,
    }]
}]

def iteration_over_user(quotes_to_calculate, results, memo):
    if len(quotes_to_calculate) == 0:
        return results

    user = quotes_to_calculate[0]
    total = 0
    total += calculate_total_per_user(user["products"], total, memo)
    results.append({"user_id": user["user_id"], "total": total })
    return iteration_over_user(quotes_to_calculate[1:], results, memo)

def calculate_total_per_user(products, total, memo):
    if len(products) == 0:
        return total

    if product := list(filter(lambda product: product["product_name"] == products[0]["product_name"], memo)):
        # print("si funciona")
        return product[0]["total"]

    products[0]["price_before_taxes"] += calculate_taxes(products[0]["price_before_taxes"], TAXES, 0)
    memo.append({ "product_name": products[0]["product_name"], "total": products[0]["price_before_taxes"] })
    # print(memo)
    total += products[0]["price_before_taxes"] + calculate_total_per_user(products[1:], total, memo)
    return total

def calculate_taxes(subtotal, taxes, total_taxes):
    if len(taxes) == 0:
        return total_taxes

    tax = taxes[0]["value"]
    total_taxes += (subtotal * tax)/100
    return calculate_taxes(subtotal, taxes[1:], total_taxes)


def main():
    number_of_repetitions = int(input("Chose a number of repetitions for the list quotes_to_calculate:"))
    number_of_repetitions = 1 if number_of_repetitions == 0 else number_of_repetitions
    results = []
    memo = []

    try:
        results_to_print = iteration_over_user(quotes_to_calculate * number_of_repetitions, results, [])
        print(results_to_print)
        print("--- %s seconds ---" % (time.time() - start_time))
    except Exception as ex:
        print("Error in the main function", str(ex))

main()