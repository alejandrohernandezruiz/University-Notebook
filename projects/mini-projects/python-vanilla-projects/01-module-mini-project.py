"""
Mini-Project 01: Industrial Motor Line Energy & Fault Monitor 
Module 01: Mutability, Control Flow, and Pythonic Loops (Pure Vanilla Python)
"""

def analyze_motor_line(
    motor_ids: list[str],
    currents: list[float],
    rpms: list[int],
    voltage: float = 400.0,
    max_current: float = 15.0,
) -> tuple[str, list[str], list[float]]:
    
    """Evaluates motor telemetry for overloads, mechanical stalls, and power usage.

    Args:
        motor_ids: Unique identifiers for each motor.
        currents: Measured electrical currents in Amperes (A).
        rpms: Measured rotational speeds in revolutions per minute (RPM).
        voltage: Nominal line voltage in Volts (V). Defaults to 400.0.
        max_current: Overload threshold in Amperes (A). Defaults to 15.0.

    Returns:
        A tuple containing (line_status, overloaded_motor_ids, power_in_kw).
    """
    
    # 1. Truthiness check: exit early if any input telemetry list is empty
    if not motor_ids or not currents or not rpms:
        return "NO_DATA", [], []

    # 2. Allocate new output structures to keep input lists immutable
    status: str = ""
    overloaded: list[str] = []
    power: list[float] = []

    # 3. Single parallel loop with strict length alignment
    for idx, (motor, current, rpm) in enumerate(
        zip(motor_ids, currents, rpms, strict=True), start=1
    ):
        # Immediate halt if a mechanical stall (< 500 RPM) is detected
        if rpm < 500:
            status = "MECHANICAL_EMERGENCY"
            print(f"[ALERT] Step {idx}: Motor {motor} stalled at {rpm} RPM.")
            break

        # Record motors exceeding the nominal current threshold
        if current > max_current:
            overloaded.append(motor)

        # Calculate apparent power in kilowatts (kW)
        p_kw: float = (voltage * current) / 1000.0
        power.append(round(p_kw, 2))
    else:
        # Executes only if the loop completes without hitting 'break'
        status = "RUNNING_OK"

    # 4. Walrus operator (:=) to assign and evaluate overload count in one step
    if (overloaded_count := len(overloaded)) > 0:
        print(f"Overloaded motors detected: {overloaded_count}")

    # 5. Ternary operator for concise alert classification
    alert_level: str = "HIGH" if overloaded_count >= 2 else "LOW"
    print(f"Alert level: {alert_level}")

    # 6. Return packed tuple
    return status, overloaded, power

if __name__ == "__main__":
    
    # Test Case 1: Nominal operating conditions (ok)
    ids_ok: list[str] = ["M-01", "M-02", "M-03", "M-04", "M-05"]
    currents_ok: list[float] = [14.0, 14.3, 14.8, 14.9, 14.2]
    rpms_ok: list[int] = [1000, 1100, 1150, 1050, 1030]

    status_ok, overloaded_ok, power_ok = analyze_motor_line(ids_ok, currents_ok, rpms_ok)
    
    print(f"Status: {status_ok} | Overloaded: {overloaded_ok} | Power (kW): {power_ok}\n")

    # Test Case 2: Overload on M-02 followed by a mechanical stall on M-03 (em)
    ids_em: list[str] = ["M-01", "M-02", "M-03", "M-04", "M-05"]
    currents_em: list[float] = [14.0, 18.5, 14.8, 16.0, 14.2]
    rpms_em: list[int] = [1020, 1100, 340, 1050, 1030]

    status_em, overloaded_em, power_em = analyze_motor_line(ids_em, currents_em, rpms_em)
    
    print(f"Status: {status_em} | Overloaded: {overloaded_em} | Power (kW): {power_em}\n")
