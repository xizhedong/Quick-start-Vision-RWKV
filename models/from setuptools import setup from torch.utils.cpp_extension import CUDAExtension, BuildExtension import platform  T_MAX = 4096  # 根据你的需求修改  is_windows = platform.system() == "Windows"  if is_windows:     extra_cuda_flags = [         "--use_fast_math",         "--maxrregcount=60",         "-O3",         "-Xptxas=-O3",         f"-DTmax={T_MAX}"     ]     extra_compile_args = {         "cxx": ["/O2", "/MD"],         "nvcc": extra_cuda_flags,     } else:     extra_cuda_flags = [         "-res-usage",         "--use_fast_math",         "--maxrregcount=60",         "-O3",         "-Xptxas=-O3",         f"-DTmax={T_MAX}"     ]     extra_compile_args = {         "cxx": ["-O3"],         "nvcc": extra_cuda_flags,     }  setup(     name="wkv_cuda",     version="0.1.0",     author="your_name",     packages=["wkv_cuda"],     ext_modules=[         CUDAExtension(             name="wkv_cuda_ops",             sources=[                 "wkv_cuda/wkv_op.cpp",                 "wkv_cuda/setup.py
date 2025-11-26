from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension
import platform

T_MAX = 4096  # 根据你的需求修改

is_windows = platform.system() == "Windows"

if is_windows:
    extra_cuda_flags = [
        "-res-usage"
        "--use_fast_math",
        "--maxrregcount=60",
        "-O3",
        "-Xptxas=-O3",
        f"-DTmax={T_MAX}"
    ]
    extra_compile_args = {
        "cxx": ["/O2", "/MD"],
        "nvcc": extra_cuda_flags,
    }
else:
    extra_cuda_flags = [
        "-res-usage",
        "--use_fast_math",
        "--maxrregcount=60",
        "-O3",
        "-Xptxas=-O3",
        f"-DTmax={T_MAX}"
    ]
    extra_compile_args = {
        "cxx": ["-O3"],
        "nvcc": extra_cuda_flags,
    }

setup(
    name="wkv_cuda",
    version="0.1.0",
    author="your_name",
    packages=["wkv_cuda"],
    ext_modules=[
        CUDAExtension(
            name="wkv_cuda_ops",
            sources=[
                "cuda/wkv_op.cpp",
                "cuda/wkv_cuda.cu"
            ],
            extra_compile_args=extra_compile_args,
        )
    ],
    cmdclass={"build_ext": BuildExtension},
)
