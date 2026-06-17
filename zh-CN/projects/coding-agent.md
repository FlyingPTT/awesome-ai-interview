# 项目：Coding Agent

## 目标

构建一个 Agent：可以检查代码库、定位 bug、编辑代码、运行测试，并总结 patch。

## 架构

- Issue parser。
- Repository search。
- File reader。
- Patch editor。
- Test runner。
- Repair loop。
- Diff summarizer。

## 技术亮点

- 有边界的 retry loop。
- Test-first diagnosis。
- 文件级变更约束。
- 高风险命令人工确认。
- 带验证证据的 patch summary。

## 简历 Bullet

实现 Coding Agent，支持仓库 issue 定位、代码编辑、目标测试运行和 verified patch summary，并加入 bounded repair loop 与命令安全控制。

