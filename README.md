# Sberbank test task

|    | kindName      | otherKindName | count_all | count_unique | dt_min  | dt_max   | dt_avg  |
|----|---------------|---------------|-----------|--------------|---------|----------|---------|
| 0  | taskNew       | taskDelivered | 240       | 240          | 0       | 0        | 0       |
| 1  | taskDelivered | taskOperation | 1056      | 240          | 0       | 7775000  | 1830930 |
| 2  | taskOperation | taskAssigned  | 751       | 240          | 0       | 57717000 | 2884334 |
| 3  | taskAssigned  | taskCostSpent | 751       | 240          | 602000  | 57777000 | 3775764 |
| 4  | taskCostSpent | taskCostSpent | 592       | 240          | 602000  | 56191000 | 3146103 |
| 5  | taskCostSpent | taskComplete  | 1042      | 237          | 602000  | 7943000  | 2447031 |
| 6  | taskComplete  | taskDelivered | 820       | 237          | 662000  | 7775000  | 2377650 |
| 7  | taskOperation | taskSupported | 305       | 237          | 1262000 | 6109000  | 1647990 |
| 8  | taskSupported | taskSupported | 237       | 237          | 1262000 | 5150000  | 1521485 |
| 9  | taskSupported | taskCostSpent | 464       | 237          | 1262000 | 57777000 | 3180480 |
| 10 | taskCostSpent | taskSupported | 159       | 159          | 3257000 | 57777000 | 6120163 |
| 11 | taskComplete  | taskFinished  | 222       | 222          | 1388000 | 7943000  | 3724396 |