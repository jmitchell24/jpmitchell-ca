---
title: "Standard Byte Units"
tags: [guide]
draft: true 
date: 2025-03-26
updated: 2025-03-26
---

# Decimal Units 

| Name      | Unit | Total Bytes               |
| --------- | ---- | ------------------------- |
| Exabytes  | EB   | 1,000,000,000,000,000,000 |
| Petabytes | PB   | 1,000,000,000,000,000     |
| Terabytes | TB   | 1,000,000,000,000         |
| Gigabytes | GB   | 1,000,000,000             |
| Megabytes | MB   | 1,000,000                 |
| Kilobytes | KB   | 1,000                     | 

# Binary Units

| Name | Unit | Magnitude | Total Bytes               |
| ---- | ---- | --------- | ------------------------- |
| ...  | EiB  | 2^60      | 1,152,921,504,606,846,976 |
| ...  | PiB  | 2^50      | 1,125,899,906,842,624     |
| ...  | TiB  | 2^40      | 1,099,511,627,776         |
| ...  | GiB  | 2^30      | 1,073,741,824             |
| ...  | MiB  | 2^20      | 1,048,576                 |
| ...  | KiB  | 2^10      | 1,024                     |


# Generating Bytes String 
``` c++
inline static std::string createBytesString(size_t bytes)
{

    size_t constexpr b10 = size_t(1) << 10;
    size_t constexpr b20 = size_t(1) << 20;
    size_t constexpr b30 = size_t(1) << 30;
    size_t constexpr b40 = size_t(1) << 40;
    size_t constexpr b50 = size_t(1) << 50;
    size_t constexpr b60 = size_t(1) << 60;

  

    if (bytes < b10) return std::to_string(bytes) + " bytes";
    else if (bytes < b20) return std::to_string(bytes / b10) + " KiB";
    else if (bytes < b30) return std::to_string(bytes / b20) + " MiB";
    else if (bytes < b40) return std::to_string(bytes / b30) + " GiB";
    else if (bytes < b50) return std::to_string(bytes / b40) + " TiB";
    else if (bytes < b60) return std::to_string(bytes / b50) + " PiB";
    return std::to_string(bytes / b60) + " EiB";
}
```