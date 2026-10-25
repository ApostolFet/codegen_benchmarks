# Бенчмарки генерации python кода

## Актуалные результаты

### Данные окружения:

```sh
pyperf collect_metadata
```

```
Metadata:
- aslr: Full randomization
- boot_time: 2026-10-25 11:18:34
- cpu_config: 0-11=driver:intel_pstate, intel_pstate:no turbo, governor:performance; idle:intel_idle
- cpu_count: 12
- cpu_freq: 0=1520 MHz; 1,3,6-7=2000 MHz; 2=1447 MHz; 4=1849 MHz; 5=662 MHz; 8=1175 MHz; 9-11=1500 MHz
- cpu_model_name: 12th Gen Intel(R) Core(TM) i5-12450H
- cpu_temp: coretemp:Package id 0=51 C, coretemp:Core 0=51 C
- date: 2026-10-25 12:00:25.082086
- load_avg_1min: 0.23
- mem_max_rss: 20.8 MiB
- perf_version: 2.10.0
- platform: Linux-7.0.0-38-generic-x86_64-with-glibc2.39
- python_cflags: -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -g -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -fstack-protector-strong -fstack-clash-protection -Wformat -Werror=format-security -fcf-protection -g -fwrapv -O2
- python_compiler: GCC 13.3.0
- python_config_args: '--enable-shared' '--prefix=/usr' '--libdir=/usr/lib/x86_64-linux-gnu' '--enable-ipv6' '--enable-loadable-sqlite-extensions' '--with-dbmliborder=bdb:gdbm' '--with-computed-gotos' '--without-ensurepip' '--with-system-expat' '--with-system-libmpdec=no' 'MKDIR_P=/bin/mkdir -p' 'CC=x86_64-linux-gnu-gcc' 'CFLAGS=-g -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -fstack-protector-strong -fstack-clash-protection -Wformat -Werror=format-security -fcf-protection ' 'LDFLAGS=-Wl,-Bsymbolic-functions -g -fwrapv -O2 ' 'CPPFLAGS=-Wdate-time -D_FORTIFY_SOURCE=3'
- python_implementation: cpython
- python_version: 3.14.9 (64-bit)
- runnable_threads: 1
- timer: clock_gettime(CLOCK_MONOTONIC), resolution: 1.00 ns
- uptime: 41 min 51.1 sec
```

Предварительно был выполнен `pyperf system tune`

```sh
pyperf system show
```

```
System state
============

CPU: use 12 logical CPUs: 0-11
Perf event: Maximum sample rate: 1 per second
ASLR: Full randomization
Linux scheduler: No CPU is isolated
CPU Frequency: 0-7=min=max=2000 MHz; 8-11=min=max=1500 MHz
IRQ affinity: Default IRQ affinity: CPU 0-11
IRQ affinity: IRQ affinity: IRQ 0-16,27,36,43,120-123,131,139-140,153-154,167-169=CPU 0-11; IRQ 141,161=CPU 6; IRQ 142,162=CPU 7; IRQ 143,155=CPU 0; IRQ 144,156=CPU 1; IRQ 145,157=CPU 2; IRQ 146,158=CPU 3; IRQ 147,159=CPU 4; IRQ 148,160=CPU 5; IRQ 149,163=CPU 8; IRQ 150,164=CPU 9; IRQ 151,165=CPU 10; IRQ 152,166=CPU 11
Power supply: the power cable is plugged
CPU scaling governor: 0-11=performance
Turbo Boost (intel_pstate): Turbo Boost disabled

Advices
=======

Linux scheduler: Use isolcpus=<cpu list> kernel parameter to isolate CPUs
Linux scheduler: Use rcu_nocbs=<cpu list> kernel parameter (with isolcpus) to not schedule RCU on isolated CPUs

OK! System ready for benchmarking
```

### Результаты

#### Кодогенерация условия
```
+-------------------+--------+------------------------+-----------------------+
| Benchmark         | base   | codegen                | separate_func         |
+===================+========+========================+=======================+
| condition/runtime | 174 ns | 137 ns: 1.27x faster   | 136 ns: 1.27x faster  |
+-------------------+--------+------------------------+-----------------------+
| condition/startup | 694 ns | 32.9 us: 47.36x slower | 1.60 us: 2.30x slower |
+-------------------+--------+------------------------+-----------------------+
```


#### Кодогенерация цикла
```
+----------------+---------+-------------------------+
| Benchmark      | base    | codegen                 |
+================+=========+=========================+
| loop/runtime   | 23.4 us | 19.3 us: 1.21x faster   |
+----------------+---------+-------------------------+
| loop/startup   | 24.2 us | 3.33 ms: 138.01x slower |
+----------------+---------+-------------------------+
```

#### Кодогенерация в `wrap_injection` dishka
```
+-------------------------------+---------+-----------------------+
| Benchmark                     | base    | codegen               |
+===============================+=========+=======================+
| dishka_wrap_injection/runtime | 4.47 us | 3.71 us: 1.20x faster |
+-------------------------------+---------+-----------------------+
| dishka_wrap_injection/startup | 965 us  | 1.36 ms: 1.40x slower |
+-------------------------------+---------+-----------------------+
```
## Как запустить бенчамарки 

1. Создаем виртуальное оружение и устанавливаем пакет (python>=3.10):

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -e .
```

2. Опционально, настроить систему для запуска бенчмарков (для минимализации влияния системы):
```sh
python -m pyperf system tune
```

Для проверки успешной настройки системы выполняется команда:
```sh
python -m pyperf system show
```
В конце вывода должно быть: `OK! System ready for benchmarking`

3. Запуск всех бенчмарков:
```sh
. ./scripts/run_all_benchmarks.sh
```

5. Опционально, откатываем настройки системы обратно:
```sh
python -m pyperf system reset
```

6. Все результаты бенчмарков сохраняются в files/, повторно посмотреть результаты:
```sh
. ./scripts/view_all_result.sh
```
