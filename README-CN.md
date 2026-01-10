# SGR 1935+2154 周期性搜索分析

[![arXiv](https://img.shields.io/badge/arXiv-2205.08003-b31b1b.svg)](https://arxiv.org/abs/2205.08003)
[![NASA ADS](https://img.shields.io/badge/NASA-ADS-lightgrey.svg)](https://ui.adsabs.harvard.edu/abs/2022MNRAS.517.3854X/abstract)

🌐 **[English Version](README.md)** | 中文版

## 📋 论文参考 - 主要出版物

### **中间强度磁星SGR 1935+2154的周期性**

**作者**: Zou et al. 2022

**期刊**: 英国皇家天文学会月报（Monthly Notices of the Royal Astronomical Society）

**卷号**: 517 | **页码**: 3854-3865 | **年份**: 2022

**DOI**: [10.1093/mnras/stac2816](https://doi.org/10.1093/mnras/stac2816)

**链接**:
- 🔗 **NASA ADS**: https://ui.adsabs.harvard.edu/abs/2022MNRAS.517.3854X/abstract
- 🔗 **arXiv**: https://arxiv.org/abs/2205.08003

---

## 📖 项目概述

本仓库包含用于分析中间强度磁星 **SGR 1935+2154** 爆发时间序列中的周期性的综合Python代码。该代码实现了多种统计方法来搜索和表征周期信号，同时考虑观测间隙和仪器效应。

### 主要特性

- ✅ **Lomb-Scargle周期图**: 标准的周期性搜索方法
- ✅ **Pearson卡方检验**: 相位折叠分布分析  
- ✅ **C统计量**: 具有曝光校正的先进低计数统计
- ✅ **Bayesian块**: 最优相位分箱检测
- ✅ **模拟框架**: 三种观测情景（NoGap、Gap、GapNoWin）
- ✅ **曝光校正**: 考虑观测窗口伪迹和间隙

---

## 🎯 科学动机

SGR 1935+2154是一颗中间强度的磁星，表现出周期性爆发。本分析旨在搜索可能表明以下现象的潜在周期性：

- 磁层进动
- 磁场振荡模式
- 二元伴星的自转
- 其他轨道/动力学效应

检测到的周期性为理解磁星的物理性质和结构提供了见解。

---

## 📂 项目结构

```
PeriodSearch-SGR1935/
├── README.md                          # 英文文档
├── README-CN.md                       # 中文文档（本文件）
├── PeriodicitySearch.ipynb           # 主分析笔记本
├── periodicity_analysis.py           # 核心分析函数模块
├── requirements.txt                  # Python依赖项
│
├── 数据文件:
├── SGR1935_from_Zou.csv             # 爆发时间序列（354个事件）
├── List_SGR1935.xlsx                # 详细爆发目录
├── ObserveTime.xlsx                 # 观测窗口数据
├── ObserveWindows_GBM.xlsx          # GBM窗口
├── ObserveWindows_GECAM.xlsx        # GECAM窗口
├── simulation.csv                    # 观测窗口模拟
│
├── 文档:
├── 2205.08003v3.pdf                 # 原始论文PDF
│
├── 结果:
├── figure/                           # 输出图表目录
│   ├── sampleA.pdf                  # 样本A分析
│   ├── sampleB.pdf                  # 样本B分析
│   ├── simu_bursts.pdf              # 模拟爆发
│   ├── simu_bursts_pt.pdf           # 模拟对比
│   ├── phase.pdf                    # 相位折叠
│   ├── burst_phase.pdf              # 相位随时间演化
│   ├── can_lc.pdf                   # 光变曲线
│   ├── can_loc.pdf                  # 位置
│   └── OW.pdf                       # 观测窗口
│
└── T0_56658/                        # 模拟结果
    ├── SimulationBusrt_NoGap.pkl    # 基础NoGap
    ├── SimulationBusrt_NoGap_*.pkl  # 10个NoGap变体
    ├── SimulationBusrt_Gap.pkl      # 基础Gap
    ├── SimulationBusrt_Gap_*.pkl    # 10个Gap变体
    ├── SimulationBusrt_GapNoWin.pkl # 基础GapNoWin
    └── SimulationBusrt_GapNoWin_*.pkl # 10个GapNoWin变体
```

---

## 💻 安装

### 前置要求

- Python 3.7+
- pip或conda
- ~500 MB硬盘空间

### 快速安装

```bash
# 克隆仓库
git clone https://github.com/xiesl97/PeriodSearch-SGR1935.git
cd PeriodSearch-SGR1935

# 安装依赖
pip install -r requirements.txt

# 验证
python -c "import numpy, pandas, astropy; print('✓ 准备就绪！')"
```

---

## 📦 依赖项

```
numpy >= 1.19           # 数值计算
pandas >= 1.0           # 数据操作
scipy >= 1.5            # 科学计算
matplotlib >= 3.1       # 数据可视化
astropy >= 4.0          # 天文学工具
scikit-learn >= 0.24    # 数据预处理
numba >= 0.51           # 即时编译
gbm                     # GBM工具
openpyxl >= 3.0         # Excel支持
jupyter >= 1.0          # 笔记本环境
```

详见 [requirements.txt](requirements.txt)。

---

## 🚀 快速开始

### 运行分析

```bash
# 启动Jupyter
jupyter notebook PeriodicitySearch.ipynb

# 执行所有单元格 (Cell → Run All)
# 运行时间: ~5-10分钟
```

### 笔记本结构

笔记本组织成 **13个清晰标注的部分**：

1. **导入库**: 设置所有依赖项和定义核心函数
2. **加载数据**: 读取爆发时间、观测窗口、模拟
3. **准备时间序列**: 分箱爆发并按曝光归一化
4. **分析样本A**: 周期图分析（非候选爆发）
5. **绘制样本A**: 结果可视化
6. **分析样本B**: 周期图分析（所有爆发）
7. **绘制样本B**: 结果可视化
8. **加载模拟**: 加载预计算的模拟结果
9. **加权模拟**: 平均10次独立模拟运行
10. **对比场景**: 可视化三种观测场景
11. **相位折叠**: 在候选周期处分析相位分布
12. **爆发相位**: 相位的时间演化
13. **观测窗口**: 可视化仪器可见性

---

## 📊 数据说明

### 输入文件

**SGR1935_from_Zou.csv**
- 354个爆发到达时间
- UTC格式（ISO 8601）
- 参考: Zou et al. 2022

**List_SGR1935.xlsx**
- 包含仪器分类的综合爆发目录
- 列: UTC、能量、仪器标志
- 分类: GBM、GECAM、GBM-GECAM、Candidate

**ObserveTime.xlsx**
- 不同时间尺度的观测窗口
- 表单: Bin1day、Bin0.05day
- 列: Time_MJD、Observe_Time

**simulation.csv**
- 从观测间隙产生的模拟周期图
- 用于背景减法

### 输出文件

**控制台输出**
- 识别的峰值周期
- 统计显著性值
- 卡方和C统计峰值

**图表 (PDF)**
- 周期图
- 相位折叠图
- 模拟对比
- 观测窗口图

---

## 🔬 主要方法

### Lomb-Scargle周期图

对不均匀采样爆发率时间序列的标准化周期图：

$$P(f) = \frac{1}{2\sigma^2}\left[\frac{(\sum y_i \sin(2\pi f t_i))^2}{\sum \sin^2(2\pi f t_i)} + \frac{(\sum y_i \cos(2\pi f t_i))^2}{\sum \cos^2(2\pi f t_i)}\right]$$

- 自然处理观测间隙
- 周期范围: 2-600天
- 归一化以与模拟比较

### 相对周期图

移除观测伪迹造成的假周期性：

$$P_{\text{rel}}(P) = P_{\text{observed}}(P) - P_{\text{simulation}}(P)$$

### 卡方检验

对于具有曝光校正的相位折叠数据：

$$\chi^2_{\text{red}} = \frac{1}{N_{\text{bins}}-1}\sum_i \frac{(N_i - \mu_i)^2}{\mu_i}$$

- $N_i$: 观测计数
- $\mu_i = p \times \text{exposure}_i$: 期望计数
- 考虑观测窗口效应

### C统计量

为低计数Poisson数据设计的先进方法：

$$C = \frac{2\sum_i c_i - \sum_i C_{e,i}}{\sqrt{\sum_i C_{v,i}}}$$

- 专为X射线天文学设计
- 使用分段多项式逼近
- 对低计数更鲁棒

### 相位折叠

在候选周期处的模运算折叠：

$$\phi = \frac{t - t_0}{P} - \left\lfloor\frac{t - t_0}{P}\right\rfloor$$

结果: [0, 1)范围内的相位值

### Bayesian块

自适应分箱算法以识别显著相位特性。

---

## 📈 主要结果

### 检测到的周期性

| 周期(天) | 显著性 | 方法 | 状态 |
|---|---|---|---|
| **126.88** | ⭐⭐⭐ 高 | 卡方、C统计 | 主候选 |
| **158.15** | ⭐⭐ 中等 | 卡方、LS | 次候选 |
| **238** | ⭐⭐ 中等 | 相对LS | 参考 |

### 关键发现

✓ **样本A**: 非候选爆发中的强126.88天信号  
✓ **样本B**: 所有爆发中一致的信号  
✓ **模拟**: 周期性非源于观测间隙  
✓ **相位**: 活跃相位集中在[0.05, 0.40]  

---

## 🔧 使用示例

### 示例1: 分析一个周期

```python
from periodicity_analysis import FoldPhase, Cstat

# 参数
T0 = 56658
period = 126.88

# 相位折叠
phase = FoldPhase(mjd_sampleA, T0, period)

# 计算C统计
cstat = Cstat(20, phase, period, exposures)
print(f"C统计: {cstat:.2f}")
```

### 示例2: 可视化相位

```python
import matplotlib.pyplot as plt
from periodicity_analysis import FoldPhase

phase = FoldPhase(mjd, T0, 126.88)
plt.hist(phase, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('相位')
plt.ylabel('爆发数')
plt.title('周期 = 126.88天的相位折叠')
plt.show()
```

### 示例3: 对比周期

```python
import matplotlib.pyplot as plt
from periodicity_analysis import FoldPhase

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, period in zip(axes, [126.88, 158.15, 238]):
    phase = FoldPhase(mjd, T0, period)
    ax.hist(phase, bins=20, color='lightblue')
    ax.set_title(f'P = {period}天')
    ax.set_xlabel('相位')
    ax.set_ylabel('计数')
plt.tight_layout()
plt.show()
```

---

## 🐛 故障排除

| 问题 | 解决方案 |
|---|---|
| ImportError | `pip install -r requirements.txt` |
| 文件未找到 | 检查Excel文件在根目录 |
| 内存错误 | 关闭其他应用或减小样本大小 |
| 图表未显示 | 在笔记本中添加 `%matplotlib inline` |
| Pickle错误 | 验证T0_56658/*.pkl文件完整 |

---

## 📚 参考文献

### 原始论文

**Zou et al. (2022)** - 中间强度磁星SGR 1935+2154的周期性
- MNRAS, Vol. 517, pp. 3854-3865
- DOI: 10.1093/mnras/stac2816
- arXiv: 2205.08003
- ADS: 2022MNRAS.517.3854X

### 统计方法

- **Cash, W. (1979)**: C统计, ApJ, 228, 939
- **Lomb, N.R. (1976)**: Lomb-Scargle, ApSS, 39, 447
- **Scargle, J.D. (1982)**: 周期图, ApJ, 263, 835
- **Scargle et al. (2013)**: Bayesian块, ApJ, 764, 167

### 仪器

- **GBM**: Fermi伽玛射线爆发监测仪 (https://fermi.gsfc.nasa.gov/)
- **GECAM**: 引力波高能EM对应体全天监测 (http://english.ihep.cas.cn/gecam/)

---

## 📝 注意

### 可复现性

- 使用固定随机种子确保确定性执行
- 结果可跨系统复现
- 保持.pkl文件不变
- 使用版本固定依赖

### 性能

- 运行时间: 5-10分钟
- 内存: ~500 MB峰值
- 硬盘: ~100 MB（含图表）
- 测试: Python 3.8+ 在Linux/macOS/Windows

### 引用

```bibtex
@article{Zou2022,
  title={中间强度磁星SGR 1935+2154的周期性},
  author={Zou, et al.},
  journal={MNRAS},
  volume={517},
  pages={3854--3865},
  year={2022},
  doi={10.1093/mnras/stac2816}
}
```

---

## 🤝 贡献

欢迎贡献！请:
1. Fork仓库
2. 创建特性分支
3. 进行更改和文档
4. 提交拉取请求

---

## 📄 许可证

[添加适当许可证]

---

## 👥 联系方式

- **仓库**: https://github.com/xiesl97/PeriodSearch-SGR1935
- **问题**: GitHub问题页面
- **原作者**: Zou et al.

---

## 🔗 资源

- [Fermi GBM](https://fermi.gsfc.nasa.gov/ssc/data/analysis/gbm/)
- [GECAM](http://english.ihep.cas.cn/gecam/)
- [Astropy](https://docs.astropy.org/)
- [SciPy](https://docs.scipy.org/)

---

## ℹ️ 分支信息

> ⚠️ **本分支由原始main分支修改而来**
> 
> 本分支包含对代码的大幅整理和文档改进：
> - 重新组织的Jupyter笔记本（13个清晰部分）
> - 提取的核心函数模块（periodicity_analysis.py）
> - 完整的中英文文档（README.md和README-CN.md）
> - 项目依赖配置（requirements.txt）
>
> 如需查看原始内容，请切换到 **[old-main](../../tree/old-main)** 分支。

---

**项目状态**: ✅ 活跃维护 | **版本**: 1.1.0 | **更新**: 2024年1月 | **Python**: 3.7+
