#!/bin/bash

# 定義顏色
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}正在建立 Docker 映像檔...${NC}"
docker compose build

echo -e "${GREEN}本地測試啟動中 (http://localhost)...${NC}"
docker compose up -d

echo -e "${GREEN}完成！請確認本地運行狀況後執行 Git Push 觸發自動化部署。${NC}"