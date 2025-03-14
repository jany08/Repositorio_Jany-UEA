def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.

    Args:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float, optional): El porcentaje de descuento. Defaults to 10.

    Returns:
        float: El monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

def main():
    # Llamada a la función con monto total y porcentaje de descuento predeterminado (10%)
    monto_total = 100
    porcentaje_descuento = 10  # Se usa el valor predeterminado
    descuento = calcular_descuento(monto_total)
    monto_final = monto_total - descuento
    print(f"Monto total: ${monto_total:.2f}")
    print(f"Descuento ({porcentaje_descuento}%): ${descuento:.2f}")
    print(f"Monto final a pagar: ${monto_final:.2f}")
    print()

    # Llamada a la función con monto total y porcentaje de descuento personalizado
    monto_total = 200
    porcentaje_descuento = 20
    descuento = calcular_descuento(monto_total, porcentaje_descuento)
    monto_final = monto_total - descuento
    print(f"Monto total: ${monto_total:.2f}")
    print(f"Descuento ({porcentaje_descuento}%): ${descuento:.2f}")
    print(f"Monto final a pagar: ${monto_final:.2f}")

if "_name_" == "_main_":
    main()