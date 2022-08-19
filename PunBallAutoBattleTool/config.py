# -*- coding: utf-8 -*-
# @Path : C:\Users\zengf\AppData\Local\Programs\Python\Python39
# @Time : 2022/4/25 18:49
# @Author : zengf
# @Email : 944458157@qq.com
# @File : config.py
# @Project : workspace

SerialNumber = {"V9D4C18424001837": "Huawei_Nova3e",
                "5c406a69": "Oneplus_9",
                "6TP7XSYX79Z9958X": "Realme_GT_Neo",
                "R5CN90FQDRX": "Samsung_A51",
                "R28M61D72RH": "Samsung_s10",
                "ce071717f19f08d40b7e": "Samsung_Note8",
                "0000020d2c5b874e": "Vivo_X30",
                "9e1940a": "Vivo_U3",
                "7ce0cc22": "Oppo_R15s",
                "9c13c818": "Oppo_R11t",
                "d014298e": "Oppo_Find_X",
                "2fd7b39a": "Oppo_Reno3",
                "9889954659504e394a": "Samsung_s8",
                "94060e1c": "Vivo_Z5x",
                "000001f5f6633d4e": "vivo_Y70s"}
PunBallDeviceToken = {"Huawei_Nova3e": "f5c481ee2c07ca9259265527e06fb503",
                      "Oneplus_9": "fd2b61f64d569ea41f8c574e0eae43d1",
                      "Realme_GT_Neo": "d2605d1fa969ee7a8b7aa8fb43aa2ebc",
                      "Samsung_A51": "1d38177047b1a9f375aca9e7eaa4b035",
                      "Samsung_S10": "c32afe8bca31f210307c221ed52ed4ca",
                      "Samsung_Note8": "9053d2ab125149be768598130a580500",
                      "Vivo_X30": "d83628c469a24fedd02bfaac5c5ff28d",
                      "Vivo_U3": "60097f25edf34cb659d42e871ba620fa",
                      "Oppo_R15s": "9053d2ab125149be768598130a580500",
                      "Oppo_R11t": "9e1031012d3607b6e9028c4948668511",
                      "Oppo_Find_X": "892d055d5f7dd4add4c53adaaba2e8f1",
                      "Oppo_Reno3": "412aabd783d9dcd5b57fed2867097183",
                      "Samsung_S8": "e0372a7642eca61f29c36525f46a3739",
                      "Vivo_Z5x": "86d0ca049247dee3c52d83bea0005140",
                      "Vivo_Y70s": "7e47bb939cde89169a7f8988ea8c5aa0"}

TOKEN = '4ac910fa1fb74d69bf664b08d98bb2ea336633171eb7475ba05b83400c9d5e63'
STF1 = 'curl -X POST --header "Content-Type: application/json" --data "{\\"serial\\":\\"'
STF2 = '\\"}" -H "Authorization: Bearer '
URL = '" http://172.16.18.94:7100/api/v1/user/devices'
ONLINE1 = 'curl -X GET --header "Content-Type: application/json" -H "Authorization: Bearer '
ONLINE2 = '" http://172.16.18.94:7100/api/v1/devices'
CONNECT1 = 'curl -X POST --header "Content-Type: application/json" -H "Authorization: Bearer '
DisCONNECT = 'curl -X DELETE --header "Content-Type: application/json" -H "Authorization: Bearer '
CONNECT2 = '/'
CONNECT3 = '/remoteConnect'

ComIP = '172.16.18.219'
ComPORT = 22
ComUSERNAME = 'HabbyQA'
ComPASSWORD = 'habby2019'
BAT_RUNNER_PATH = "D:\\workspace\\PunBallAutoBattleTool\\deviceRunner.bat"
DirPath = "D:\\airtest-case\\"

