"""
Mini-Project 02: Warehouse Spare Parts & Maintenance Audit
Modules 01 & 02: Set Algebra, Hash Lookups, Comprehensions & Extended Unpacking
"""

def audit_plant_operations(
    warehouse_a: list[str],
    warehouse_b: list[str],
    stock_levels: dict[str, int],
    telemetry_logs: list[dict[str, str | float]],
    critical_vibration: float = 5.0,
) -> dict[str, object]:
    
    """
    Audits warehouse inventory against machine telemetry for critical alerts.

    Args:
        warehouse_a: Part SKUs scanned in Warehouse A (may contain duplicates).
        warehouse_b: Part SKUs scanned in Warehouse B (may contain duplicates).
        stock_levels: Mapping of part_sku -> available inventory quantity.
        telemetry_logs: Raw sensor events containing sensor_id, part_sku, and vibration.
        critical_vibration: Vibration threshold requiring part replacement. Defaults to 5.0.

    Returns:
        A structured audit report dictionary containing inventory sets, critical alerts,
        restock lists, and boundary vibration readings.
    """
    
    # 1. Truthiness check: exit early if any required dataset is empty
    if not warehouse_a or not warehouse_b or not stock_levels or not telemetry_logs:
        return {}

    # 2. Warehouse Set Algebra: deduplicate scans and compute intersections/differences
    parts_a: set[str] = set(warehouse_a)
    parts_b: set[str] = set(warehouse_b)

    shared_skus: set[str] = parts_a & parts_b
    exclusive_a: set[str] = parts_a - parts_b

    # 3. Telemetry Filtering & Comprehensions
    # Single-pass set comprehension to extract unique sensor family prefixes
    sensor_families: set[str] = {
        str(log["sensor_id"]).split("-")[0] for log in telemetry_logs
    }

    # Dict comprehension filtering only readings at or above the critical threshold
    critical_alerts: dict[str, float] = {
        str(log["part_sku"]): float(log["vibration"])
        for log in telemetry_logs
        if float(log["vibration"]) >= critical_vibration
    }

    # 4. Stock Cross-Referencing & Safe Hash Lookups
    restock_needed: list[str] = []

    for idx, (part_sku, vibration) in enumerate(critical_alerts.items(), start=1):
        # Safe .get() lookup defaults to 0 if the SKU is missing from the catalog
        current_stock: int = stock_levels.get(part_sku, 0)
        print(
            f"[ALERT #{idx}] Part {part_sku} | Vibration: {vibration:.2f} | Stock: {current_stock}"
        )

        if current_stock == 0:
            restock_needed.append(part_sku)

    # Walrus operator (:=) to evaluate and report urgent restock count in one step
    if (urgent_count := len(restock_needed)) > 0:
        print(
            f"[URGENT] Restock required for {urgent_count} part(s): {', '.join(restock_needed)}\n"
        )

    # 5. Signal Extraction & Extended Unpacking
    all_vibrations: list[float] = [float(log["vibration"]) for log in telemetry_logs]

    if len(all_vibrations) >= 2:
        first_vibration, *middle_vibrations, last_vibration = all_vibrations
    else:
        first_vibration = last_vibration = all_vibrations
        middle_vibrations = []

    # 6. Return structured audit report
    return {
        "shared_skus": shared_skus,
        "exclusive_warehouse_a": exclusive_a,
        "sensor_families": sensor_families,
        "critical_alerts": critical_alerts,
        "restock_needed": restock_needed,
        "first_vibration": first_vibration,
        "middle_vibrations": middle_vibrations,
        "latest_vibration": last_vibration,
    }


if __name__ == "__main__":
    # Sample plant telemetry and warehouse scan datasets
    wh_a: list[str] = ["BRG-404", "VLV-102", "MTR-900", "BRG-404", "SNS-110"]
    wh_b: list[str] = ["VLV-102", "PMP-305", "SNS-110", "PMP-305"]

    inventory: dict[str, int] = {
        "BRG-404": 0,
        "VLV-102": 14,
        "MTR-900": 3,
        "PMP-305": 5,
        # "SNS-110" is intentionally omitted to verify safe .get() fallback behavior
    }

    logs: list[dict[str, str | float]] = [
        {"sensor_id": "VIB-01", "part_sku": "BRG-404", "vibration": 6.4},
        {"sensor_id": "TEMP-04", "part_sku": "VLV-102", "vibration": 2.1},
        {"sensor_id": "VIB-02", "part_sku": "SNS-110", "vibration": 5.8},
        {"sensor_id": "PRS-09", "part_sku": "MTR-900", "vibration": 3.5},
    ]

    # Execute audit and display formatted report
    audit_report: dict[str, object] = audit_plant_operations(
        wh_a, wh_b, inventory, logs, critical_vibration=5.0
    )

    print("--- AUDIT SUMMARY REPORT ---")
    for key, value in audit_report.items():
        print(f"{key}: {value}")
