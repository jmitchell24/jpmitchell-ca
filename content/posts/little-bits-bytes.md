---
title: "Little bits of Bytes (and Bits)"
tags: [guide]
draft: false
date: 2025-03-26
updated: 2025-06-03
---

### Decimal Units 

{% table() %}
| Name      | Unit | Total Bytes               |
| --------- | ---- | ------------------------- |
| Exabytes  | EB   | 1,000,000,000,000,000,000 |
| Petabytes | PB   | 1,000,000,000,000,000     |
| Terabytes | TB   | 1,000,000,000,000         |
| Gigabytes | GB   | 1,000,000,000             |
| Megabytes | MB   | 1,000,000                 |
| Kilobytes | KB   | 1,000                     | 
{% end %}

### Binary Units

{% table() %}
| Name | Unit | Magnitude | Total Bytes |
| ---- | ---- | --------- | ------------------------- |
| Exbibyte | EiB | 2^60 | 1,152,921,504,606,846,976 |
| Pebibyte | PiB | 2^50 | 1,125,899,906,842,624 |
| Tebibyte | TiB | 2^40 | 1,099,511,627,776 |
| Gibibyte | GiB | 2^30 | 1,073,741,824 |
| Mebibyte | MiB | 2^20 | 1,048,576 |
| Kibibyte | KiB | 2^10 | 1,024 |
{% end %}

### Generating Byte String 

#### C++ 
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

#### Python 
``` python 
def create_bytes_string(bytes):
    b10 = 1 << 10  
    b20 = 1 << 20  
    b30 = 1 << 30  
    b40 = 1 << 40  
    b50 = 1 << 50  
    b60 = 1 << 60  
    
    if bytes < b10:
        return f"{bytes} bytes"
    elif bytes < b20:
        return f"{bytes // b10} KiB"
    elif bytes < b30:
        return f"{bytes // b20} MiB"
    elif bytes < b40:
        return f"{bytes // b30} GiB"
    elif bytes < b50:
        return f"{bytes // b40} TiB"
    elif bytes < b60:
        return f"{bytes // b50} PiB"
    return f"{bytes // b60} EiB"
```