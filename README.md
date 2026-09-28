# Бенчмарки генерации python кода

## Актуалные результаты

### Данные окружения:

```sh
pyperf collect_metadata
```

```
Metadata:
- aslr: Full randomization
- boot_time: 2026-09-28 15:19:51
- cpu_config: 0-11=driver:intel_pstate, intel_pstate:no turbo, governor:performance; idle:intel_idle
- cpu_count: 12
- cpu_freq: 0=1818 MHz; 1-3,5,7=2000 MHz; 4=1288 MHz; 6=1714 MHz; 8=1294 MHz; 9=1166 MHz; 10-11=1500 MHz
- cpu_model_name: 12th Gen Intel(R) Core(TM) i5-12450H
- cpu_temp: coretemp:Package id 0=35 C, coretemp:Core 0=34 C
- date: 2026-09-28 15:42:30.584080
- load_avg_1min: 0.21
- mem_max_rss: 20.7 MiB
- perf_version: 2.10.0
- platform: Linux-7.0.0-34-generic-x86_64-with-glibc2.39
- python_cflags: -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -g -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -fstack-protector-strong -fstack-clash-protection -Wformat -Werror=format-security -fcf-protection -g -fwrapv -O2
- python_compiler: GCC 13.3.0
- python_config_args: '--enable-shared' '--prefix=/usr' '--libdir=/usr/lib/x86_64-linux-gnu' '--enable-ipv6' '--enable-loadable-sqlite-extensions' '--with-dbmliborder=bdb:gdbm' '--with-computed-gotos' '--without-ensurepip' '--with-system-expat' '--with-system-libmpdec=no' 'MKDIR_P=/bin/mkdir -p' 'CC=x86_64-linux-gnu-gcc' 'CFLAGS=-g -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -fstack-protector-strong -fstack-clash-protection -Wformat -Werror=format-security -fcf-protection ' 'LDFLAGS=-Wl,-Bsymbolic-functions -g -fwrapv -O2 ' 'CPPFLAGS=-Wdate-time -D_FORTIFY_SOURCE=3'
- python_implementation: cpython
- python_version: 3.14.6 (64-bit)
- runnable_threads: 1
- timer: clock_gettime(CLOCK_MONOTONIC), resolution: 1.00 ns
- uptime: 22 min 39.6 sec
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
IRQ affinity: IRQ affinity: IRQ 0-16,27,36,43,120-123,131,139,152-154,167-169=CPU 0-11; IRQ 140,161=CPU 6; IRQ 141,162=CPU 7; IRQ 142,155=CPU 0; IRQ 143,156=CPU 1; IRQ 144,157=CPU 2; IRQ 145,158=CPU 3; IRQ 146,159=CPU 4; IRQ 147,160=CPU 5; IRQ 148,163=CPU 8; IRQ 149,164=CPU 9; IRQ 150,165=CPU 10; IRQ 151,166=CPU 11
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
| condition/runtime | 184 ns | 136 ns: 1.36x faster   | 136 ns: 1.36x faster  |
+-------------------+--------+------------------------+-----------------------+
| condition/startup | 743 ns | 33.6 us: 45.19x slower | 1.72 us: 2.32x slower |
+-------------------+--------+------------------------+-----------------------+
| Geometric mean    | (ref)  | 5.76x slower           | 1.31x slower          |
+-------------------+--------+------------------------+-----------------------+
```


#### Кодогенерация цикла
```
+----------------+---------+-------------------------+
| Benchmark      | base    | codegen                 |
+================+=========+=========================+
| loop/runtime   | 24.1 us | 19.4 us: 1.24x faster   |
+----------------+---------+-------------------------+
| loop/startup   | 24.7 us | 3.27 ms: 132.08x slower |
+----------------+---------+-------------------------+
| Geometric mean | (ref)   | 10.32x slower           |
+----------------+---------+-------------------------+
```

#### Кодогенерация в `wrap_injection` dishka
```
+-------------------------------+---------+-----------------------+
| Benchmark                     | base    | codegen               |
+===============================+=========+=======================+
| dishka_wrap_injection/runtime | 2.97 us | 2.39 us: 1.24x faster |
+-------------------------------+---------+-----------------------+
| dishka_wrap_injection/startup | 510 us  | 845 us: 1.66x slower  |
+-------------------------------+---------+-----------------------+
| Geometric mean                | (ref)   | 1.16x slower          |
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
