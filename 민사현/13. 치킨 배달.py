{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "903b3c76",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 13. 치킨 배달\n",
    "\n",
    "from itertools import combinations\n",
    "\n",
    "# 집, 치킨집 좌표\n",
    "n, m = map(int,input().split())\n",
    "house, chicken = [], []\n",
    "\n",
    "for i in range(n):\n",
    "    data = list(map(int, input().split()))\n",
    "    for j in range(n):\n",
    "        if data[j] == 1: # 1:house\n",
    "            house.append((i,j))\n",
    "        elif data[j] == 2: # 2:chicken\n",
    "            chicken.append((i,j))\n",
    "            \n",
    "# m개 치킨집만 영업\n",
    "winner = list(combinations(chicken, m))\n",
    "\n",
    "# 치킨거리\n",
    "def chicken_dis(winner):\n",
    "    result = 0\n",
    "    for hx, hy in house:\n",
    "        tmp = float('inf')\n",
    "        for cx, xy in chicken:\n",
    "            tmp = min(tmp, abs(hx-cx) + abs(hy-cy))\n",
    "        result += tmp\n",
    "    return result\n",
    "\n",
    "result = float('inf')\n",
    "for w in winner:\n",
    "    result = min(result, chicken_dis(w))\n",
    "    \n",
    "print(result)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
