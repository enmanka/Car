/*
 Navicat Premium Data Transfer

 Source Server         : zcx
 Source Server Type    : MySQL
 Source Server Version : 80015
 Source Host           : localhost:3306
 Source Schema         : house

 Target Server Type    : MySQL
 Target Server Version : 80015
 File Encoding         : 65001

 Date: 18/05/2019 20:57:28
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bank_trend
-- ----------------------------
DROP TABLE IF EXISTS `bank_trend`;
CREATE TABLE `bank_trend`  (
  `amount` double DEFAULT NULL,
  `year` text CHARACTER SET utf8 COLLATE utf8_bin,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of bank_trend
-- ----------------------------
INSERT INTO `bank_trend` VALUES (27080543.290000003, '2016', 1);
INSERT INTO `bank_trend` VALUES (71786680.15, '2017', 2);
INSERT INTO `bank_trend` VALUES (981121.45, '2018', 3);

-- ----------------------------
-- Table structure for city_count
-- ----------------------------
DROP TABLE IF EXISTS `city_count`;
CREATE TABLE `city_count`  (
  `city` text CHARACTER SET utf8 COLLATE utf8_bin,
  `count` bigint(20) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of city_count
-- ----------------------------
INSERT INTO `city_count` VALUES ('福州', 6357, 1);
INSERT INTO `city_count` VALUES ('重庆', 33892, 2);
INSERT INTO `city_count` VALUES ('广州', 19493, 3);
INSERT INTO `city_count` VALUES ('贵阳', 2829, 4);
INSERT INTO `city_count` VALUES ('兰州', 1153, 5);
INSERT INTO `city_count` VALUES ('石家庄', 10287, 6);
INSERT INTO `city_count` VALUES ('长沙', 979, 7);
INSERT INTO `city_count` VALUES ('长春', 5019, 8);
INSERT INTO `city_count` VALUES ('银川', 1937, 9);
INSERT INTO `city_count` VALUES ('沈阳', 6059, 10);
INSERT INTO `city_count` VALUES ('呼和浩特', 2097, 11);
INSERT INTO `city_count` VALUES ('成都', 21018, 12);
INSERT INTO `city_count` VALUES ('济南', 12215, 13);
INSERT INTO `city_count` VALUES ('天津', 36444, 14);
INSERT INTO `city_count` VALUES ('昆明', 2786, 15);
INSERT INTO `city_count` VALUES ('杭州', 18950, 16);
INSERT INTO `city_count` VALUES ('北京', 27481, 17);
INSERT INTO `city_count` VALUES ('合肥', 20611, 18);
INSERT INTO `city_count` VALUES ('南宁', 1506, 19);
INSERT INTO `city_count` VALUES ('海口', 621, 20);
INSERT INTO `city_count` VALUES ('武汉', 28140, 21);
INSERT INTO `city_count` VALUES ('郑州', 18070, 22);
INSERT INTO `city_count` VALUES ('南京', 20495, 23);
INSERT INTO `city_count` VALUES ('哈尔滨', 1396, 24);
INSERT INTO `city_count` VALUES ('上海', 32982, 25);
INSERT INTO `city_count` VALUES ('南昌', 2954, 26);
INSERT INTO `city_count` VALUES ('西安', 12218, 27);
INSERT INTO `city_count` VALUES ('太原', 3478, 28);

-- ----------------------------
-- Table structure for company_amont
-- ----------------------------
DROP TABLE IF EXISTS `company_amont`;
CREATE TABLE `company_amont`  (
  `amount` double DEFAULT NULL,
  `company_name` text CHARACTER SET utf8 COLLATE utf8_bin,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of company_amont
-- ----------------------------
INSERT INTO `company_amont` VALUES (61934919.73, '中行锦江支行', 1);
INSERT INTO `company_amont` VALUES (17490172.79, '建设银行成都市第二支行', 2);
INSERT INTO `company_amont` VALUES (20423252.370000005, '成都银行华兴支行', 3);

-- ----------------------------
-- Table structure for company_sorted
-- ----------------------------
DROP TABLE IF EXISTS `company_sorted`;
CREATE TABLE `company_sorted`  (
  `city` text CHARACTER SET utf8 COLLATE utf8_bin,
  `score` double DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of company_sorted
-- ----------------------------
INSERT INTO `company_sorted` VALUES ('成都中铁二局瑞城物业管理有限公司', 320, 1);
INSERT INTO `company_sorted` VALUES ('四川永泰物业有限责任公司', 165, 2);
INSERT INTO `company_sorted` VALUES ('成都和协物业服务有限公司', 240, 3);
INSERT INTO `company_sorted` VALUES ('成都中能物业管理有限责任公司', 395, 4);
INSERT INTO `company_sorted` VALUES ('成都仁和春天物业管理有限公司', 250, 5);
INSERT INTO `company_sorted` VALUES ('四川昌达物业管理有限责任公司', 135, 6);
INSERT INTO `company_sorted` VALUES ('成都市绿园物业管理有限公司', 85, 7);
INSERT INTO `company_sorted` VALUES ('成都富力物业管理有限责任公司', 450, 8);
INSERT INTO `company_sorted` VALUES ('四川悦华置地物业管理有限公司', 525, 9);
INSERT INTO `company_sorted` VALUES ('深圳市保利物业管理集团有限公司成都分公司', 160, 10);
INSERT INTO `company_sorted` VALUES ('成都新和志远物业管理有限责任公司', 75, 11);
INSERT INTO `company_sorted` VALUES ('成都兴成物业管理有限公司', 180, 12);
INSERT INTO `company_sorted` VALUES ('四川省宏冶资产管理有限公司', 230, 13);
INSERT INTO `company_sorted` VALUES ('中海物业管理有限公司成都分公司', 340, 14);
INSERT INTO `company_sorted` VALUES ('四川天府绿洲物业管理有限责任公司', 530, 15);
INSERT INTO `company_sorted` VALUES ('成都惠好物业管理有限公司', 110, 16);
INSERT INTO `company_sorted` VALUES ('成都市恒德物业服务有限公司', 75, 17);
INSERT INTO `company_sorted` VALUES ('四川舜苑资产经营管理有限责任公司', 220, 18);
INSERT INTO `company_sorted` VALUES ('成都星弘物业管理有限公司', 105, 19);
INSERT INTO `company_sorted` VALUES ('成都中天盛鸿物业服务有限公司', 355, 20);
INSERT INTO `company_sorted` VALUES ('四川东晨物业发展有限公司', 230, 21);
INSERT INTO `company_sorted` VALUES ('成都高立物业管理有限公司', 350, 22);
INSERT INTO `company_sorted` VALUES ('成都励志一行物业服务有限公司', 345, 23);
INSERT INTO `company_sorted` VALUES ('成都市金澳物业管理有限公司', 105, 24);
INSERT INTO `company_sorted` VALUES ('成都凯旋物业服务有限责任公司', 510, 25);
INSERT INTO `company_sorted` VALUES ('成都交大智能物业管理有限公司', 450, 26);
INSERT INTO `company_sorted` VALUES ('成都衡信英伦物业管理有限公司', 70, 27);
INSERT INTO `company_sorted` VALUES ('成都夏利文物业管理有限公司', 120, 28);
INSERT INTO `company_sorted` VALUES ('成都成飞物业服务有限责任公司', 555, 29);
INSERT INTO `company_sorted` VALUES ('四川博南商务服务有限公司', 220, 30);
INSERT INTO `company_sorted` VALUES ('成都锦官新城物业管理有限责任公司', 445, 31);
INSERT INTO `company_sorted` VALUES ('成都家发物业管理有限公司', 105, 32);
INSERT INTO `company_sorted` VALUES ('成都安捷通物业管理有限公司', 275, 33);
INSERT INTO `company_sorted` VALUES ('成都市弘瑞物业服务有限公司', 105, 34);
INSERT INTO `company_sorted` VALUES ('广东金诺物业管理服务有限公司成都分公司', 230, 35);
INSERT INTO `company_sorted` VALUES ('深圳市百利行物业发展有限公司成都分公司', 230, 36);
INSERT INTO `company_sorted` VALUES ('四川力宝企业管理有限公司', 1900, 37);
INSERT INTO `company_sorted` VALUES ('成都汇川物业服务有限公司', 110, 38);
INSERT INTO `company_sorted` VALUES ('成都市尚都物业服务有限公司', 120, 39);
INSERT INTO `company_sorted` VALUES ('四川艾明物业管理有限公司', 435, 40);
INSERT INTO `company_sorted` VALUES ('成都同悦荟商业管理有限公司', 195, 41);
INSERT INTO `company_sorted` VALUES ('北京城承物业管理有限责任公司成都分公司', 130, 42);
INSERT INTO `company_sorted` VALUES ('四川浩宅物业管理有限公司', 120, 43);
INSERT INTO `company_sorted` VALUES ('成都市鑫鹏物业服务有限公司', 85, 44);
INSERT INTO `company_sorted` VALUES ('成都金信物业管理有限责任公司', 110, 45);
INSERT INTO `company_sorted` VALUES ('成都万科锦西置业有限公司', 85, 46);
INSERT INTO `company_sorted` VALUES ('成都富房不动产房屋经纪连锁有限公司', 50, 47);
INSERT INTO `company_sorted` VALUES ('成都房邻居房地产经纪有限公司', 70, 48);
INSERT INTO `company_sorted` VALUES ('成都赛博特置业投资发展有限公司', 85, 49);
INSERT INTO `company_sorted` VALUES ('成都新成国际经济发展有限公司', 80, 50);
INSERT INTO `company_sorted` VALUES ('成都中铁业兴房地产开发有限公司', 80, 51);
INSERT INTO `company_sorted` VALUES ('成都住家叁陆伍房地产经纪有限公司', 85, 52);
INSERT INTO `company_sorted` VALUES ('简阳市馨雅房介服务部', 75, 53);
INSERT INTO `company_sorted` VALUES ('简阳市谊城房地产经纪有限公司', 75, 54);
INSERT INTO `company_sorted` VALUES ('简阳市房好家房地产中介服务有限公司', 75, 55);
INSERT INTO `company_sorted` VALUES ('成都碧宇物业服务有限公司', 85, 56);
INSERT INTO `company_sorted` VALUES ('成都华凌物业管理有限公司', 220, 57);
INSERT INTO `company_sorted` VALUES ('四川圣康物业管理有限公司', 340, 58);
INSERT INTO `company_sorted` VALUES ('成都康泰物业管理服务有限公司', 110, 59);
INSERT INTO `company_sorted` VALUES ('四川民兴物业管理有限公司', 820, 60);
INSERT INTO `company_sorted` VALUES ('戴德梁行房地产咨询（成都）有限公司', 120, 61);
INSERT INTO `company_sorted` VALUES ('成都世豪新瑞物业服务有限公司', 70, 62);
INSERT INTO `company_sorted` VALUES ('成都恒扬物业服务有限公司', 195, 63);
INSERT INTO `company_sorted` VALUES ('四川火炬物业管理有限公司', 435, 64);
INSERT INTO `company_sorted` VALUES ('中电建五兴物业管理有限公司', 445, 65);
INSERT INTO `company_sorted` VALUES ('四川蜀府东润物业服务有限公司', 345, 66);
INSERT INTO `company_sorted` VALUES ('成都金开房屋经营管理有限公司', 240, 67);
INSERT INTO `company_sorted` VALUES ('邛崃市金益物业有限公司', 85, 68);
INSERT INTO `company_sorted` VALUES ('邛崃市翔运物业管理有限公司', 220, 69);
INSERT INTO `company_sorted` VALUES ('招商局物业管理有限公司成都分公司', 220, 70);
INSERT INTO `company_sorted` VALUES ('四川高路物业服务有限公司', 345, 71);
INSERT INTO `company_sorted` VALUES ('成都金房物业集团有限责任公司', 565, 72);
INSERT INTO `company_sorted` VALUES ('四川骅阳物业服务有限公司', 230, 73);
INSERT INTO `company_sorted` VALUES ('成都盛禾物业服务有限公司', 120, 74);
INSERT INTO `company_sorted` VALUES ('成都卓望嘉物业服务有限公司', 260, 75);
INSERT INTO `company_sorted` VALUES ('成都民信物业管理有限公司', 110, 76);
INSERT INTO `company_sorted` VALUES ('四川省祥荣物业管理有限公司', 85, 77);
INSERT INTO `company_sorted` VALUES ('成都市华声物业服务有限公司', 85, 78);
INSERT INTO `company_sorted` VALUES ('彭州市福田物业发展有限责任公司', 345, 79);
INSERT INTO `company_sorted` VALUES ('成都好当家物业服务有限公司', 215, 80);
INSERT INTO `company_sorted` VALUES ('成都广泽物业服务有限公司', 230, 81);
INSERT INTO `company_sorted` VALUES ('成都德士卫物业管理有限公司', 220, 82);
INSERT INTO `company_sorted` VALUES ('成都汇融物业服务有限公司', 235, 83);
INSERT INTO `company_sorted` VALUES ('成都万科物业服务有限公司', 2900, 84);
INSERT INTO `company_sorted` VALUES ('成都庭明物业服务有限公司', 245, 85);
INSERT INTO `company_sorted` VALUES ('四川瑞德物业发展有限公司', 430, 86);
INSERT INTO `company_sorted` VALUES ('成都珠江物业经营管理有限公司', 110, 87);
INSERT INTO `company_sorted` VALUES ('第一太平戴维斯物业顾问（北京）有限公司成都分公司', 225, 88);
INSERT INTO `company_sorted` VALUES ('成都华云物业服务有限公司', 75, 89);
INSERT INTO `company_sorted` VALUES ('成都市众合物业服务有限公司', 330, 90);
INSERT INTO `company_sorted` VALUES ('成都瑞庭物业服务有限公司', 105, 91);
INSERT INTO `company_sorted` VALUES ('成都江丰物业管理有限公司', 105, 92);
INSERT INTO `company_sorted` VALUES ('成都富临物业管理有限责任公司', 365, 93);
INSERT INTO `company_sorted` VALUES ('深圳市花样年国际物业服务有限公司成都分公司', 150, 94);
INSERT INTO `company_sorted` VALUES ('成都市森宇物业有限责任公司', 240, 95);
INSERT INTO `company_sorted` VALUES ('成都孺牛物业服务有限公司', 190, 96);
INSERT INTO `company_sorted` VALUES ('怡家园（厦门）物业管理有限公司成都分公司', 140, 97);
INSERT INTO `company_sorted` VALUES ('四川伦华物业服务有限公司', 105, 98);
INSERT INTO `company_sorted` VALUES ('成都天恒物业管理有限责任公司', 230, 99);
INSERT INTO `company_sorted` VALUES ('四川圣爱融创资产管理有限公司', 390, 100);
INSERT INTO `company_sorted` VALUES ('成都麦高物业经营管理有限公司', 215, 101);
INSERT INTO `company_sorted` VALUES ('成都忠信物业管理有限公司', 495, 102);
INSERT INTO `company_sorted` VALUES ('成都佶惠佳物业服务有限公司', 245, 103);
INSERT INTO `company_sorted` VALUES ('四川万联物业管理有限公司', 380, 104);
INSERT INTO `company_sorted` VALUES ('四川华玮物业管理有限公司', 640, 105);
INSERT INTO `company_sorted` VALUES ('成都强讯新和房地产开发有限公司', 80, 106);
INSERT INTO `company_sorted` VALUES ('成都众益嘉房地产经纪有限公司', 75, 107);
INSERT INTO `company_sorted` VALUES ('四川联兴房地产开发有限公司', 170, 108);
INSERT INTO `company_sorted` VALUES ('成都辰诗置业有限公司', 85, 109);
INSERT INTO `company_sorted` VALUES ('宁波市亚太酒店物业管理有限公司简阳分公司', 85, 110);
INSERT INTO `company_sorted` VALUES ('四川省都江堰辰一物业有限公司', 85, 111);
INSERT INTO `company_sorted` VALUES ('四川省国嘉物业服务有限公司', 300, 112);
INSERT INTO `company_sorted` VALUES ('四川翼丰资产管理有限公司', 130, 113);
INSERT INTO `company_sorted` VALUES ('成都高投世纪物业服务有限公司', 240, 114);
INSERT INTO `company_sorted` VALUES ('成都市仕和物业服务有限公司', 105, 115);
INSERT INTO `company_sorted` VALUES ('成都川信物业管理有限公司', 115, 116);
INSERT INTO `company_sorted` VALUES ('四川洁欣新高物业服务有限公司', 240, 117);
INSERT INTO `company_sorted` VALUES ('保利物业发展股份有限公司成都分公司', 1220, 118);
INSERT INTO `company_sorted` VALUES ('成都远大创新物业管理有限责任公司', 175, 119);
INSERT INTO `company_sorted` VALUES ('成都鸟巢物业服务有限公司', 115, 120);
INSERT INTO `company_sorted` VALUES ('成都众和为物业服务有限公司', 365, 121);
INSERT INTO `company_sorted` VALUES ('四川景瑞房产经营管理有限公司', 85, 122);
INSERT INTO `company_sorted` VALUES ('成都瑞智物业管理有限公司', 110, 123);
INSERT INTO `company_sorted` VALUES ('成都家园经营管理有限公司', 575, 124);
INSERT INTO `company_sorted` VALUES ('成都鼎吉物业服务有限公司', 110, 125);
INSERT INTO `company_sorted` VALUES ('成都家和业好房产物业有限公司', 110, 126);
INSERT INTO `company_sorted` VALUES ('成都金绵物业管理有限公司', 220, 127);
INSERT INTO `company_sorted` VALUES ('成都居安物业服务有限责任公司', 390, 128);
INSERT INTO `company_sorted` VALUES ('世茂天成物业服务集团有限公司成都第二分公司', 130, 129);
INSERT INTO `company_sorted` VALUES ('成都洁华物业管理有限公司', 585, 130);
INSERT INTO `company_sorted` VALUES ('成都德冠物业管理有限公司', 135, 131);
INSERT INTO `company_sorted` VALUES ('成都大周天房地产有限责任公司', 70, 132);
INSERT INTO `company_sorted` VALUES ('成都弘民物业管理有限公司', 130, 133);
INSERT INTO `company_sorted` VALUES ('成都嘉善商务服务管理有限公司', 520, 134);
INSERT INTO `company_sorted` VALUES ('四川嘉宝资产管理集团股份有限公司', 690, 135);
INSERT INTO `company_sorted` VALUES ('四川远鸿物业管理有限公司', 245, 136);
INSERT INTO `company_sorted` VALUES ('成都海科物业管理有限公司', 230, 137);
INSERT INTO `company_sorted` VALUES ('成都市壹贰服务产业有限公司', 120, 138);
INSERT INTO `company_sorted` VALUES ('四川瑞云物业管理服务有限公司', 405, 139);
INSERT INTO `company_sorted` VALUES ('成都好斯佳物业管理有限公司', 110, 140);
INSERT INTO `company_sorted` VALUES ('成都坤和物业咨询发展有限公司', 255, 141);
INSERT INTO `company_sorted` VALUES ('中房集团成都物业有限公司', 120, 142);
INSERT INTO `company_sorted` VALUES ('成都安特物业管理有限公司', 110, 143);
INSERT INTO `company_sorted` VALUES ('成都华居物业管理有限公司', 120, 144);
INSERT INTO `company_sorted` VALUES ('成都元海物业管理有限公司', 105, 145);
INSERT INTO `company_sorted` VALUES ('成都量力企业管理服务有限公司', 115, 146);
INSERT INTO `company_sorted` VALUES ('四川邦泰物业服务有限公司', 235, 147);
INSERT INTO `company_sorted` VALUES ('成都蔚蓝卡地亚物业管理有限公司', 110, 148);
INSERT INTO `company_sorted` VALUES ('成都德昌行物业服务有限公司', 260, 149);
INSERT INTO `company_sorted` VALUES ('成都市好日子物业服务有限公司', 110, 150);
INSERT INTO `company_sorted` VALUES ('成都祥福物业管理有限公司', 340, 151);
INSERT INTO `company_sorted` VALUES ('成都天天物业管理有限公司', 110, 152);
INSERT INTO `company_sorted` VALUES ('成都永发鑫乐鑫物业服务有限公司', 110, 153);
INSERT INTO `company_sorted` VALUES ('广州海伦堡物业管理有限公司成都分公司', 105, 154);
INSERT INTO `company_sorted` VALUES ('成都市中骏物业管理有限公司', 380, 155);
INSERT INTO `company_sorted` VALUES ('仲量联行测量师事务所（上海）有限公司成都分公司', 135, 156);
INSERT INTO `company_sorted` VALUES ('成都锐志蜀新物业管理有限公司', 105, 157);
INSERT INTO `company_sorted` VALUES ('成都海凌物业管理有限公司', 85, 158);
INSERT INTO `company_sorted` VALUES ('四川佳友物业有限责任公司', 240, 159);
INSERT INTO `company_sorted` VALUES ('成都锦淮物业管理有限公司', 85, 160);
INSERT INTO `company_sorted` VALUES ('中海物业管理有限公司成都中海振兴分公司', 275, 161);
INSERT INTO `company_sorted` VALUES ('成都鸿博物业咨询服务有限公司', 340, 162);
INSERT INTO `company_sorted` VALUES ('成都市协和物业管理有限公司', 110, 163);
INSERT INTO `company_sorted` VALUES ('四川福晟物业管理有限公司', 120, 164);
INSERT INTO `company_sorted` VALUES ('成都鼎瑞物业服务有限公司', 430, 165);
INSERT INTO `company_sorted` VALUES ('成都花园物业管理有限责任公司', 390, 166);
INSERT INTO `company_sorted` VALUES ('四川景灿物业服务有限公司', 220, 167);
INSERT INTO `company_sorted` VALUES ('成都合力物业服务有限公司', 215, 168);
INSERT INTO `company_sorted` VALUES ('成都市清华坊楼宇服务有限责任公司', 595, 169);
INSERT INTO `company_sorted` VALUES ('四川致和物业服务有限公司', 225, 170);
INSERT INTO `company_sorted` VALUES ('四川川音物业管理有限公司', 215, 171);
INSERT INTO `company_sorted` VALUES ('四川金开物业管理有限公司', 110, 172);
INSERT INTO `company_sorted` VALUES ('成都心连心物业管理有限公司', 360, 173);
INSERT INTO `company_sorted` VALUES ('成都爱地阳光物业管理有限公司', 120, 174);
INSERT INTO `company_sorted` VALUES ('成都尉洪物业服务有限公司', 315, 175);
INSERT INTO `company_sorted` VALUES ('成都合智合力物业管理有限公司', 220, 176);
INSERT INTO `company_sorted` VALUES ('成都合智商务服务有限公司', 380, 177);
INSERT INTO `company_sorted` VALUES ('成都双流华兴住宅物业发展有限公司', 85, 178);
INSERT INTO `company_sorted` VALUES ('重庆国奥村物业服务有限公司成都分公司', 195, 179);
INSERT INTO `company_sorted` VALUES ('成都公德物业管理有限公司', 360, 180);
INSERT INTO `company_sorted` VALUES ('成都耐心物业管理有限公司', 365, 181);
INSERT INTO `company_sorted` VALUES ('成都市鑫美源实业有限责任公司', 130, 182);
INSERT INTO `company_sorted` VALUES ('成都晟玥物业管理有限公司', 215, 183);
INSERT INTO `company_sorted` VALUES ('成都市居安乐物业服务有限公司', 555, 184);
INSERT INTO `company_sorted` VALUES ('成都利丰物业有限公司', 475, 185);
INSERT INTO `company_sorted` VALUES ('金碧物业有限公司成都分公司', 480, 186);
INSERT INTO `company_sorted` VALUES ('成都怡家园物业管理有限公司', 360, 187);
INSERT INTO `company_sorted` VALUES ('成都天和物业管理有限公司 ', 85, 188);
INSERT INTO `company_sorted` VALUES ('成都市东景物业管理有限公司', 450, 189);
INSERT INTO `company_sorted` VALUES ('四川川衡房地产估价有限公司', 85, 190);
INSERT INTO `company_sorted` VALUES ('成都复鑫泰商贸有限公司', 85, 191);
INSERT INTO `company_sorted` VALUES ('中粮地产集团深圳物业管理有限公司成都分公司', 380, 192);
INSERT INTO `company_sorted` VALUES ('吉祥房产', 90, 193);
INSERT INTO `company_sorted` VALUES ('简阳市简城镇新鑫屋房介服务', 75, 194);
INSERT INTO `company_sorted` VALUES ('成都市金港物业管理有限责任公司', 515, 195);
INSERT INTO `company_sorted` VALUES ('金堂县赵镇好又多房屋信息部', 75, 196);
INSERT INTO `company_sorted` VALUES ('四川长青物业策划有限公司', 180, 197);
INSERT INTO `company_sorted` VALUES ('四川鹏筑置业有限公司', 80, 198);
INSERT INTO `company_sorted` VALUES ('成都世茂新城房地产开发有限公司', 80, 199);
INSERT INTO `company_sorted` VALUES ('成都富博房地产开发有限公司', 90, 200);
INSERT INTO `company_sorted` VALUES ('四川德源房地产开发有限公司', 85, 201);
INSERT INTO `company_sorted` VALUES ('成都大唐晶座房地产经纪有限公司', 60, 202);
INSERT INTO `company_sorted` VALUES ('四川万心联合房地产营销策划有限公司', 85, 203);
INSERT INTO `company_sorted` VALUES ('四川恒丰物业管理有限公司', 195, 204);
INSERT INTO `company_sorted` VALUES ('深圳市华侨城物业服务有限公司成都分公司', 255, 205);
INSERT INTO `company_sorted` VALUES ('成都大兴业房地产经纪有限公司', 90, 206);
INSERT INTO `company_sorted` VALUES ('成都市诚沁物业管理有限责任公司', 225, 207);
INSERT INTO `company_sorted` VALUES ('成都友帮物业管理有限公司', 105, 208);
INSERT INTO `company_sorted` VALUES ('成都市百佳安物业管理有限公司', 90, 209);
INSERT INTO `company_sorted` VALUES ('四川五好物业服务有限公司', 390, 210);
INSERT INTO `company_sorted` VALUES ('成都军苑物业管理有限公司', 110, 211);
INSERT INTO `company_sorted` VALUES ('成都蜀信物业服务有限公司', 520, 212);
INSERT INTO `company_sorted` VALUES ('成都诚尚物业管理有限公司', 115, 213);
INSERT INTO `company_sorted` VALUES ('成都可信物业管理有限公司', 75, 214);
INSERT INTO `company_sorted` VALUES ('深圳威士达物业发展有限公司成都分公司', 105, 215);
INSERT INTO `company_sorted` VALUES ('成都亿龙物业有限公司', 105, 216);
INSERT INTO `company_sorted` VALUES ('四川佳和物业管理有限公司', 120, 217);
INSERT INTO `company_sorted` VALUES ('中电建物业管理有限公司成都分公司', 470, 218);
INSERT INTO `company_sorted` VALUES ('成都市联众物业管理有限公司', 340, 219);
INSERT INTO `company_sorted` VALUES ('四川青禾物业管理有限公司', 95, 220);
INSERT INTO `company_sorted` VALUES ('成都江南物业管理有限公司', 110, 221);
INSERT INTO `company_sorted` VALUES ('成都欣欣物业管理服务有限公司', 105, 222);
INSERT INTO `company_sorted` VALUES ('成都麓山物业管理有限公司', 155, 223);
INSERT INTO `company_sorted` VALUES ('深圳市中信物业管理有限公司成都分公司', 310, 224);
INSERT INTO `company_sorted` VALUES ('成都麦迪亚物业服务有限责任公司', 260, 225);
INSERT INTO `company_sorted` VALUES ('中铁建（北京）物业管理有限公司成都分公司', 410, 226);
INSERT INTO `company_sorted` VALUES ('成都润祥物业管理服务有限公司', 105, 227);
INSERT INTO `company_sorted` VALUES ('成都亿新物业管理有限公司', 265, 228);
INSERT INTO `company_sorted` VALUES ('四川省嘉丽来物业管理有限责任公司', 85, 229);
INSERT INTO `company_sorted` VALUES ('成都林森物业管理有限公司', 200, 230);
INSERT INTO `company_sorted` VALUES ('成都名著物业管理有限公司', 235, 231);
INSERT INTO `company_sorted` VALUES ('四川省水电集团百事吉物业管理有限公司', 120, 232);
INSERT INTO `company_sorted` VALUES ('金科物业服务集团有限公司四川分公司', 280, 233);
INSERT INTO `company_sorted` VALUES ('成都广厦物业管理有限公司', 220, 234);
INSERT INTO `company_sorted` VALUES ('四川盛德物业管理有限责任公司', 80, 235);
INSERT INTO `company_sorted` VALUES ('成都赛特物业管理有限责任公司', 200, 236);
INSERT INTO `company_sorted` VALUES ('成都瀚霖雨物业管理有限公司', 110, 237);
INSERT INTO `company_sorted` VALUES ('四川硕润酒店管理有限公司', 225, 238);
INSERT INTO `company_sorted` VALUES ('成都兴东物业管理有限公司', 85, 239);
INSERT INTO `company_sorted` VALUES ('西藏启元物业管理服务有限公司成都分公司', 110, 240);
INSERT INTO `company_sorted` VALUES ('四川派月阳物业服务有限公司', 80, 241);
INSERT INTO `company_sorted` VALUES ('成都市时代物业管理有限责任公司', 190, 242);
INSERT INTO `company_sorted` VALUES ('成都市安和物业服务有限责任公司', 255, 243);
INSERT INTO `company_sorted` VALUES ('四川华西集团物业管理有限公司', 220, 244);
INSERT INTO `company_sorted` VALUES ('成都颐丰物业管理有限责任公司', 160, 245);
INSERT INTO `company_sorted` VALUES ('深圳市彩生活物业管理有限公司成都分公司', 315, 246);
INSERT INTO `company_sorted` VALUES ('四川省仙都物业服务有限责任公司', 95, 247);
INSERT INTO `company_sorted` VALUES ('重庆天骄爱生活服务股份有限公司成都分公司', 120, 248);
INSERT INTO `company_sorted` VALUES ('成都银林物业有限公司', 80, 249);
INSERT INTO `company_sorted` VALUES ('成都万丰创新物业管理有限公司', 120, 250);
INSERT INTO `company_sorted` VALUES ('成都和佳物业管理有限公司', 430, 251);
INSERT INTO `company_sorted` VALUES ('成都吾爱物业服务有限公司', 110, 252);
INSERT INTO `company_sorted` VALUES ('成都信谊物业股份有限公司', 370, 253);
INSERT INTO `company_sorted` VALUES ('四川鼎晟资产管理有限责任公司', 565, 254);
INSERT INTO `company_sorted` VALUES ('成都同创物业管理有限公司', 115, 255);
INSERT INTO `company_sorted` VALUES ('四川通瑞投资管理有限责任公司', 85, 256);
INSERT INTO `company_sorted` VALUES ('邛崃市竹溪物业管理有限公司', 360, 257);
INSERT INTO `company_sorted` VALUES ('成都大成英联华经营管理有限公司', 105, 258);
INSERT INTO `company_sorted` VALUES ('成都和城梵景物业发展有限公司', 110, 259);
INSERT INTO `company_sorted` VALUES ('成都市祥宇物业管理有限公司', 125, 260);
INSERT INTO `company_sorted` VALUES ('成都公信物业管理有限公司', 105, 261);
INSERT INTO `company_sorted` VALUES ('成都佳祥物业管理有限公司', 85, 262);
INSERT INTO `company_sorted` VALUES ('四川飞宇集团成都飞宇物业管理有限公司', 340, 263);
INSERT INTO `company_sorted` VALUES ('成都市双流锦丽园物业管理有限公司', 110, 264);
INSERT INTO `company_sorted` VALUES ('成都尊尼物业管理有限公司', 215, 265);
INSERT INTO `company_sorted` VALUES ('成都好人家物业有限责任公司', 260, 266);
INSERT INTO `company_sorted` VALUES ('家利物业管理（重庆）有限公司成都分公司', 495, 267);
INSERT INTO `company_sorted` VALUES ('成都睿恒物业管理有限责任公司', 260, 268);
INSERT INTO `company_sorted` VALUES ('成都明远物业发展有限公司', 130, 269);
INSERT INTO `company_sorted` VALUES ('成都乾坤物业管理有限公司', 70, 270);
INSERT INTO `company_sorted` VALUES ('成都市锦城物业服务有限责任公司', 425, 271);
INSERT INTO `company_sorted` VALUES ('成都玛雅富地房地产经纪有限公司', 80, 272);
INSERT INTO `company_sorted` VALUES ('成都宏启物业服务有限公司', 110, 273);
INSERT INTO `company_sorted` VALUES ('成都通发众好物业有限责任公司', 430, 274);
INSERT INTO `company_sorted` VALUES ('成都星晟置业有限公司', 85, 275);
INSERT INTO `company_sorted` VALUES ('成都市开成投资有限公司', 80, 276);
INSERT INTO `company_sorted` VALUES ('成都市宏升升物业管理有限公司', 105, 277);
INSERT INTO `company_sorted` VALUES ('成都市隆城物业管理有限责任公司', 85, 278);
INSERT INTO `company_sorted` VALUES ('成都龙湖锦裕置业有限公司', 80, 279);
INSERT INTO `company_sorted` VALUES ('中航物业管理有限公司成都分公司', 560, 280);
INSERT INTO `company_sorted` VALUES ('成都首创正华置业有限公司', 85, 281);
INSERT INTO `company_sorted` VALUES ('广西柳州恒信物业服务有限公司成都分公司', 110, 282);
INSERT INTO `company_sorted` VALUES ('成都鸿鹄展置业有限责任公司', 80, 283);
INSERT INTO `company_sorted` VALUES ('成都玛雅金诺房地产经纪有限公司', 75, 284);
INSERT INTO `company_sorted` VALUES ('福建伯恩物业管理股份有限公司成都分公司', 195, 285);
INSERT INTO `company_sorted` VALUES ('成都合达联行物业服务有限公司', 520, 286);
INSERT INTO `company_sorted` VALUES ('成都盛邦信息技术有限公司', 80, 287);
INSERT INTO `company_sorted` VALUES ('成都远和物业管理有限责任公司', 75, 288);
INSERT INTO `company_sorted` VALUES ('四川开元郡物业服务有限公司', 110, 289);
INSERT INTO `company_sorted` VALUES ('成都市青白江永兴物业管理有限公司', 110, 290);
INSERT INTO `company_sorted` VALUES ('成都北新物业服务有限公司', 105, 291);
INSERT INTO `company_sorted` VALUES ('四川新华物业有限公司', 415, 292);
INSERT INTO `company_sorted` VALUES ('成都欣宜物业管理有限公司', 110, 293);
INSERT INTO `company_sorted` VALUES ('四川绿水华达物业管理有限责任公司', 115, 294);
INSERT INTO `company_sorted` VALUES ('成都住邦物业有限公司', 240, 295);
INSERT INTO `company_sorted` VALUES ('成都顺畅物业管理有限公司', 105, 296);
INSERT INTO `company_sorted` VALUES ('成都双流鸿志物业有限公司', 85, 297);
INSERT INTO `company_sorted` VALUES ('成都东升福斯特物业服务有限公司', 110, 298);
INSERT INTO `company_sorted` VALUES ('成都雅丽居物业管理有限公司', 120, 299);
INSERT INTO `company_sorted` VALUES ('四川通和土地与房地产估价有限责任公司', 85, 300);
INSERT INTO `company_sorted` VALUES ('四川君安居物业服务有限公司', 75, 301);
INSERT INTO `company_sorted` VALUES ('成都云程房地产营销策划有限公司', 70, 302);
INSERT INTO `company_sorted` VALUES ('成都埃蒙斯物业管理有限公司', 105, 303);
INSERT INTO `company_sorted` VALUES ('四川省精华房地产开发有限公司', 80, 304);
INSERT INTO `company_sorted` VALUES ('成都龙湖物业服务有限公司', 495, 305);
INSERT INTO `company_sorted` VALUES ('四川中原物业顾问有限公司东苑营业部', 85, 306);
INSERT INTO `company_sorted` VALUES ('四川通用物业管理有限责任公司', 255, 307);
INSERT INTO `company_sorted` VALUES ('简阳市创居房产中介有限公司', 75, 308);
INSERT INTO `company_sorted` VALUES ('成都市嘉德联行物业服务有限公司', 125, 309);
INSERT INTO `company_sorted` VALUES ('成都讯利康旭置业有限公司', 80, 310);
INSERT INTO `company_sorted` VALUES ('成都双流百信物业管理有限责任公司', 220, 311);
INSERT INTO `company_sorted` VALUES ('成都市朗源房地产开发有限公司', 165, 312);
INSERT INTO `company_sorted` VALUES ('四川信如物业管理有限公司', 110, 313);
INSERT INTO `company_sorted` VALUES ('成都中为房地产经纪有限公司天府二街店', 85, 314);
INSERT INTO `company_sorted` VALUES ('南京朗诗物业管理有限公司成都分公司', 120, 315);
INSERT INTO `company_sorted` VALUES ('四川省润无声物业发展有限责任公司', 400, 316);
INSERT INTO `company_sorted` VALUES ('成都市金优物业服务有限责任公司', 330, 317);
INSERT INTO `company_sorted` VALUES ('成都诚悦时代物业服务有限公司', 545, 318);
INSERT INTO `company_sorted` VALUES ('成都诚信物业管理有限公司', 320, 319);
INSERT INTO `company_sorted` VALUES ('成都创艺物业有限公司', 345, 320);
INSERT INTO `company_sorted` VALUES ('南京仁恒物业管理有限公司成都分公司', 120, 321);
INSERT INTO `company_sorted` VALUES ('成都仁恒物业管理有限公司', 115, 322);
INSERT INTO `company_sorted` VALUES ('成都泓恬物业服务有限公司', 110, 323);
INSERT INTO `company_sorted` VALUES ('成都鑫元物业管理有限公司', 85, 324);
INSERT INTO `company_sorted` VALUES ('成都世纪城物业服务有限公司', 415, 325);
INSERT INTO `company_sorted` VALUES ('四川申安物业服务有限公司', 120, 326);
INSERT INTO `company_sorted` VALUES ('成都市银杏物业管理有限责任公司', 575, 327);
INSERT INTO `company_sorted` VALUES ('成都欣瑞资产管理有限公司', 160, 328);
INSERT INTO `company_sorted` VALUES ('成都百盛物业发展有限公司', 75, 329);
INSERT INTO `company_sorted` VALUES ('成都泓济物业服务有限责任公司', 560, 330);
INSERT INTO `company_sorted` VALUES ('成都勤信物业服务有限公司', 360, 331);
INSERT INTO `company_sorted` VALUES ('四川航空物业管理有限责任公司', 115, 332);
INSERT INTO `company_sorted` VALUES ('成都润琦物业管理有限公司', 105, 333);
INSERT INTO `company_sorted` VALUES ('成都市金证恒达物业服务有限公司', 220, 334);
INSERT INTO `company_sorted` VALUES ('成都银都物业服务有限公司', 315, 335);
INSERT INTO `company_sorted` VALUES ('廊坊荣盛物业服务有限公司成都分公司', 230, 336);
INSERT INTO `company_sorted` VALUES ('成都翰林物业服务有限公司', 75, 337);
INSERT INTO `company_sorted` VALUES ('成都成房物业有限公司', 430, 338);
INSERT INTO `company_sorted` VALUES ('成都市馨家物业管理有限公司', 75, 339);
INSERT INTO `company_sorted` VALUES ('成都市圣海物业服务有限公司', 120, 340);
INSERT INTO `company_sorted` VALUES ('成都家可佳商务服务有限公司', 105, 341);
INSERT INTO `company_sorted` VALUES ('四川佳年华置地有限责任公司', 90, 342);
INSERT INTO `company_sorted` VALUES ('四川瑞信物业管理有限公司', 130, 343);
INSERT INTO `company_sorted` VALUES ('成都市永平置业有限公司', 80, 344);
INSERT INTO `company_sorted` VALUES ('成都托奇物业有限公司', 75, 345);
INSERT INTO `company_sorted` VALUES ('双流美耕投资有限公司', 85, 346);
INSERT INTO `company_sorted` VALUES ('成都家联物业服务有限公司', 230, 347);
INSERT INTO `company_sorted` VALUES ('金牛区杰城房产信息部', 85, 348);
INSERT INTO `company_sorted` VALUES ('成都欧菲物业服务有限公司', 500, 349);
INSERT INTO `company_sorted` VALUES ('新都区大丰开悦新赣新房屋信息服务部', 80, 350);
INSERT INTO `company_sorted` VALUES ('成都新天地居家物业服务有限公司', 105, 351);
INSERT INTO `company_sorted` VALUES ('四川省诚卓房地产开发有限公司', 60, 352);
INSERT INTO `company_sorted` VALUES ('四川嘉豪物业管理有限公司', 75, 353);
INSERT INTO `company_sorted` VALUES ('凯雅（成都）置业有限公司', 80, 354);
INSERT INTO `company_sorted` VALUES ('成都润福祥物业管理有限公司', 85, 355);
INSERT INTO `company_sorted` VALUES ('成都太行瑞宏房地产开发有限公司', 85, 356);
INSERT INTO `company_sorted` VALUES ('成都天天佳物业服务有限公司', 105, 357);
INSERT INTO `company_sorted` VALUES ('成都瑞霖物业管理有限公司', 105, 358);
INSERT INTO `company_sorted` VALUES ('成都合能物业管理有限公司', 400, 359);
INSERT INTO `company_sorted` VALUES ('大邑聚仁物业管理有限公司', 110, 360);
INSERT INTO `company_sorted` VALUES ('成都浩佳物业服务有限公司', 195, 361);
INSERT INTO `company_sorted` VALUES ('成都市嘉晋物业管理有限公司', 110, 362);
INSERT INTO `company_sorted` VALUES ('成都通宇物业管理有限公司', 530, 363);
INSERT INTO `company_sorted` VALUES ('成都东博物业管理有限责任公司', 120, 364);
INSERT INTO `company_sorted` VALUES ('成都市公事达物业有限公司', 220, 365);
INSERT INTO `company_sorted` VALUES ('成都新合资产经营管理有限公司', 85, 366);
INSERT INTO `company_sorted` VALUES ('成都圣合物业管理有限公司', 425, 367);
INSERT INTO `company_sorted` VALUES ('重庆泓山物业管理有限公司成都分公司', 130, 368);
INSERT INTO `company_sorted` VALUES ('四川金房物业服务有限公司', 115, 369);
INSERT INTO `company_sorted` VALUES ('成都华益物业管理有限责任公司', 45, 370);
INSERT INTO `company_sorted` VALUES ('成都皇鹏物业有限责任公司', 120, 371);
INSERT INTO `company_sorted` VALUES ('成都烽森物业管理有限公司', 220, 372);
INSERT INTO `company_sorted` VALUES ('成都嘉诚新悦物业管理集团有限公司', 590, 373);
INSERT INTO `company_sorted` VALUES ('成都昱瑞物业管理有限公司', 80, 374);
INSERT INTO `company_sorted` VALUES ('成都金地物业管理有限公司', 220, 375);
INSERT INTO `company_sorted` VALUES ('成都吉利物业管理有限公司', 195, 376);
INSERT INTO `company_sorted` VALUES ('四川环诚物业管理有限公司', 220, 377);
INSERT INTO `company_sorted` VALUES ('成都瑞地企业管理有限公司', 140, 378);
INSERT INTO `company_sorted` VALUES ('金堂县惠民物业管理有限公司', 110, 379);
INSERT INTO `company_sorted` VALUES ('成都新闻物业有限责任公司', 270, 380);
INSERT INTO `company_sorted` VALUES ('成都市恒泽物业管理有限公司', 235, 381);
INSERT INTO `company_sorted` VALUES ('成都宜华置业有限公司', 85, 382);
INSERT INTO `company_sorted` VALUES ('成都尚鸿物业服务有限公司', 175, 383);
INSERT INTO `company_sorted` VALUES ('都江堰市紫霞房屋中介服务部', 80, 384);
INSERT INTO `company_sorted` VALUES ('四川万豪物业管理顾问有限公司', 75, 385);
INSERT INTO `company_sorted` VALUES ('成都众致合房地产经纪有限公司', 75, 386);
INSERT INTO `company_sorted` VALUES ('成都市荣鹏物业管理有限公司', 85, 387);
INSERT INTO `company_sorted` VALUES ('成都盛世瑞城职业有限公司', 80, 388);
INSERT INTO `company_sorted` VALUES ('自贡市英祥物业管理有限公司成都分公司', 120, 389);
INSERT INTO `company_sorted` VALUES ('成都大唐豪园房屋中介有限公司', 75, 390);
INSERT INTO `company_sorted` VALUES ('成都合德物业服务有限公司', 125, 391);
INSERT INTO `company_sorted` VALUES ('成都晟大房地产经纪有限公司', 80, 392);
INSERT INTO `company_sorted` VALUES ('成都聚烨物业管理有限公司', 85, 393);
INSERT INTO `company_sorted` VALUES ('简阳市上好家物业管理有限公司', 85, 394);
INSERT INTO `company_sorted` VALUES ('成都喜沁金沙物业管理服务有限责任公司', 225, 395);
INSERT INTO `company_sorted` VALUES ('简阳市中谊房产信息服务部', 75, 396);
INSERT INTO `company_sorted` VALUES ('成都宝利物业经营管理有限责任公司', 230, 397);
INSERT INTO `company_sorted` VALUES ('四川省佑庭英联华物业管理有限责任公司', 120, 398);
INSERT INTO `company_sorted` VALUES ('成都白华物业管理有限公司', 105, 399);
INSERT INTO `company_sorted` VALUES ('成都星宇物业管理有限公司', 105, 400);
INSERT INTO `company_sorted` VALUES ('成都创信物业管理有限公司', 110, 401);
INSERT INTO `company_sorted` VALUES ('成都润锦城实业有限公司', 240, 402);
INSERT INTO `company_sorted` VALUES ('成都丽盛物业管理有限公司', 220, 403);
INSERT INTO `company_sorted` VALUES ('成都华昌物业发展有限责任公司', 620, 404);
INSERT INTO `company_sorted` VALUES ('成都威斯顿经营管理有限责任公司', 505, 405);
INSERT INTO `company_sorted` VALUES ('成都康怡世和物业发展有限公司', 110, 406);
INSERT INTO `company_sorted` VALUES ('成都熙门物业管理有限责任公司', 110, 407);
INSERT INTO `company_sorted` VALUES ('成都市创和物业有限公司', 125, 408);
INSERT INTO `company_sorted` VALUES ('四川军盛源物业管理服务有限公司', 80, 409);
INSERT INTO `company_sorted` VALUES ('蓬溪恒辉物业管理有限公司', 70, 410);
INSERT INTO `company_sorted` VALUES ('成都三和佳物业服务有限公司', 345, 411);
INSERT INTO `company_sorted` VALUES ('成都茂瑞物业服务有限责任公司', 205, 412);
INSERT INTO `company_sorted` VALUES ('成都融信物业服务有限公司', 115, 413);
INSERT INTO `company_sorted` VALUES ('成都宏庆物业管理有限公司', 115, 414);
INSERT INTO `company_sorted` VALUES ('成都市中立房地产估价有限公司', 85, 415);
INSERT INTO `company_sorted` VALUES ('四川蜀府物业服务有限责任公司', 405, 416);
INSERT INTO `company_sorted` VALUES ('成都首善房地产经纪有限公司', 80, 417);
INSERT INTO `company_sorted` VALUES ('重庆华宇物业服务集团有限公司成都分公司', 370, 418);
INSERT INTO `company_sorted` VALUES ('金堂县赵镇红祥房屋信息部', 75, 419);
INSERT INTO `company_sorted` VALUES ('成都中海物业管理有限公司', 435, 420);
INSERT INTO `company_sorted` VALUES ('成都德商达置业有限公司', 85, 421);
INSERT INTO `company_sorted` VALUES ('成都斯诺普投资管理有限公司', 85, 422);
INSERT INTO `company_sorted` VALUES ('成都联众房地产营销策划有限公司', 75, 423);
INSERT INTO `company_sorted` VALUES ('成都市高蓉物业管理有限责任公司', 65, 424);
INSERT INTO `company_sorted` VALUES ('成都月光房地产经纪有限公司', 80, 425);
INSERT INTO `company_sorted` VALUES ('四川长虹物业服务有限责任公司成都分公司', 115, 426);
INSERT INTO `company_sorted` VALUES ('四川新景实业有限公司', 85, 427);
INSERT INTO `company_sorted` VALUES ('四川兴川投资有限公司', 65, 428);
INSERT INTO `company_sorted` VALUES ('成都威尔斯普物业管理有限公司', 105, 429);
INSERT INTO `company_sorted` VALUES ('简阳惠信物业服务有限公司', 115, 430);
INSERT INTO `company_sorted` VALUES ('深圳市中洲物业管理有限公司成都分公司', 120, 431);
INSERT INTO `company_sorted` VALUES ('成都首创锦汇置业有限公司', 85, 432);
INSERT INTO `company_sorted` VALUES ('上海上置物业集团有限公司成都分公司', 170, 433);
INSERT INTO `company_sorted` VALUES ('成都大唐房屋中介有限公司', 85, 434);
INSERT INTO `company_sorted` VALUES ('九龙仓（中国）物业管理有限公司', 250, 435);
INSERT INTO `company_sorted` VALUES ('成都科美物业管理有限公司', 120, 436);
INSERT INTO `company_sorted` VALUES ('成都众悦物业管理有限公司', 110, 437);
INSERT INTO `company_sorted` VALUES ('重庆隆鑫物业管理有限公司成都分公司', 110, 438);
INSERT INTO `company_sorted` VALUES ('成都明宇环球商业管理有限公司', 275, 439);
INSERT INTO `company_sorted` VALUES ('上海世茂南京物业服务有限公司成都第二分公司', 120, 440);
INSERT INTO `company_sorted` VALUES ('北京中铁第一太平物业服务有限公司成都分公司', 215, 441);
INSERT INTO `company_sorted` VALUES ('成都温馨园物业管理有限公司', 115, 442);
INSERT INTO `company_sorted` VALUES ('成都上实锦绣物业服务有限公司', 225, 443);
INSERT INTO `company_sorted` VALUES ('四川石油管理局', 160, 444);
INSERT INTO `company_sorted` VALUES ('华润置地（成都）物业服务有限公司', 1600, 445);
INSERT INTO `company_sorted` VALUES ('四川忠信物业管理有限公司', 120, 446);
INSERT INTO `company_sorted` VALUES ('成都怡和居物业服务有限公司', 220, 447);
INSERT INTO `company_sorted` VALUES ('成都天投物业管理有限公司', 375, 448);
INSERT INTO `company_sorted` VALUES ('成都铸信物业管理有限公司', 120, 449);
INSERT INTO `company_sorted` VALUES ('北京北大资源物业经营管理集团成都分公司', 110, 450);
INSERT INTO `company_sorted` VALUES ('鑫苑科技服务股份有限公司成都分公司', 120, 451);
INSERT INTO `company_sorted` VALUES ('成都田园物业管理有限公司', 220, 452);
INSERT INTO `company_sorted` VALUES ('四川和盟物业管理有限公司', 495, 453);
INSERT INTO `company_sorted` VALUES ('成都三和锦阳物业有限公司', 85, 454);
INSERT INTO `company_sorted` VALUES ('成都曲氏英联华物业服务有限公司', 390, 455);
INSERT INTO `company_sorted` VALUES ('成都宏润市场经营管理有限公司', 105, 456);
INSERT INTO `company_sorted` VALUES ('成都昌兴物业管理有限公司', 125, 457);
INSERT INTO `company_sorted` VALUES ('成都绿舟商务服务有限公司', 85, 458);
INSERT INTO `company_sorted` VALUES ('成都市斯培行物业服务有限公司', 220, 459);
INSERT INTO `company_sorted` VALUES ('成都中铁二局集团物业管理有限公司', 110, 460);
INSERT INTO `company_sorted` VALUES ('四川一帆风物业发展有限公司', 120, 461);
INSERT INTO `company_sorted` VALUES ('成都嘉秀物业服务有限公司', 200, 462);
INSERT INTO `company_sorted` VALUES ('成都金浣花实业有限公司', 135, 463);
INSERT INTO `company_sorted` VALUES ('成都高新区中和惠民物业服务中心', 110, 464);
INSERT INTO `company_sorted` VALUES ('中铁八局集团（成都）物业管理有限公司', 340, 465);
INSERT INTO `company_sorted` VALUES ('成都兰庭物业管理有限公司', 105, 466);
INSERT INTO `company_sorted` VALUES ('领地集团股份有限公司', 85, 467);
INSERT INTO `company_sorted` VALUES ('中海佳诚（成都）房地产开发有限公司', 85, 468);
INSERT INTO `company_sorted` VALUES ('成都市亿和物业管理有限公司', 125, 469);
INSERT INTO `company_sorted` VALUES ('国电置业有限公司四川分公司', 120, 470);
INSERT INTO `company_sorted` VALUES ('成都建业物业有限公司', 110, 471);
INSERT INTO `company_sorted` VALUES ('成都成华瑞渝置业有限公司', 85, 472);
INSERT INTO `company_sorted` VALUES ('都江堰市锦兴物业管理有限公司', 110, 473);
INSERT INTO `company_sorted` VALUES ('四川省简阳市温馨信息服务有限公司', 85, 474);
INSERT INTO `company_sorted` VALUES ('成都市恒逸物业管理有限公司', 95, 475);
INSERT INTO `company_sorted` VALUES ('简阳市鸿顺房介服务部', 75, 476);
INSERT INTO `company_sorted` VALUES ('成都市蒲江星辰物业管理有限责任公司', 85, 477);
INSERT INTO `company_sorted` VALUES ('成都湖景湾物业服务有限公司', 215, 478);
INSERT INTO `company_sorted` VALUES ('成都港联物业管理有限公司', 110, 479);
INSERT INTO `company_sorted` VALUES ('云南俊发物业服务有限公司成都分公司', 120, 480);
INSERT INTO `company_sorted` VALUES ('成都瑞亨房地产评估有限公司', 85, 481);
INSERT INTO `company_sorted` VALUES ('成都市双建物业管理有限公司', 75, 482);
INSERT INTO `company_sorted` VALUES ('华润置地（成都）青羊有限公司', 80, 483);
INSERT INTO `company_sorted` VALUES ('成都乾豪物业服务有限公司', 120, 484);
INSERT INTO `company_sorted` VALUES ('成都市能城房地产开发有限公司', 80, 485);
INSERT INTO `company_sorted` VALUES ('四川圣诚物业服务有限公司', 200, 486);
INSERT INTO `company_sorted` VALUES ('成都柳江房地产开发有限责任公司', 85, 487);
INSERT INTO `company_sorted` VALUES ('成都市新都区兴房物业管理有限公司', 105, 488);
INSERT INTO `company_sorted` VALUES ('四川世联行兴业房地产顾问有限公司', 75, 489);
INSERT INTO `company_sorted` VALUES ('家利物业管理（深圳）有限公司成都分公司', 140, 490);
INSERT INTO `company_sorted` VALUES ('成都好房优家易居房地产经纪有限公司', 75, 491);
INSERT INTO `company_sorted` VALUES ('成都兴旺宝物业服务有限公司', 105, 492);
INSERT INTO `company_sorted` VALUES ('成都西城家物业管理有限公司', 120, 493);
INSERT INTO `company_sorted` VALUES ('成都润居物业管理有限公司', 120, 494);
INSERT INTO `company_sorted` VALUES ('成都圣沅佳理物业管理有限公司', 120, 495);
INSERT INTO `company_sorted` VALUES ('成都和顺物业服务有限责任公司', 260, 496);
INSERT INTO `company_sorted` VALUES ('都江堰市南桥物业管理有限责任公司', 95, 497);
INSERT INTO `company_sorted` VALUES ('成都康普雷斯物业服务有限公司', 115, 498);
INSERT INTO `company_sorted` VALUES ('成都罗浮物业服务有限公司', 155, 499);
INSERT INTO `company_sorted` VALUES ('四川瑞诚物业服务有限公司', 105, 500);
INSERT INTO `company_sorted` VALUES ('成都祥合物业服务有限公司', 110, 501);
INSERT INTO `company_sorted` VALUES ('重庆棕榈泉联英物业服务有限公司成都分公司', 120, 502);
INSERT INTO `company_sorted` VALUES ('都江堰市青都物业管理有限责任公司', 110, 503);
INSERT INTO `company_sorted` VALUES ('长城物业集团股份有限公司成都分公司', 120, 504);
INSERT INTO `company_sorted` VALUES ('成都维德物业管理有限公司', 110, 505);
INSERT INTO `company_sorted` VALUES ('成都圣爵物业服务有限公司', 105, 506);
INSERT INTO `company_sorted` VALUES ('成都美佳物业服务有限公司', 105, 507);
INSERT INTO `company_sorted` VALUES ('成都洁兴物业管理有限公司', 120, 508);
INSERT INTO `company_sorted` VALUES ('成都双流王府物业管理有限公司', 70, 509);
INSERT INTO `company_sorted` VALUES ('四川金和总府物业管理有限公司', 120, 510);
INSERT INTO `company_sorted` VALUES ('四川兴顺物业管理有限公司', 105, 511);
INSERT INTO `company_sorted` VALUES ('成都锦东不动产投资管理有限公司', 125, 512);
INSERT INTO `company_sorted` VALUES ('四川欣辉物业服务有限公司', 80, 513);
INSERT INTO `company_sorted` VALUES ('成都美好家园物业服务有限责任公司', 180, 514);
INSERT INTO `company_sorted` VALUES ('遂宁市谐安物业服务有限公司', 105, 515);
INSERT INTO `company_sorted` VALUES ('成都亿城物业管理有限公司', 85, 516);
INSERT INTO `company_sorted` VALUES ('成都齐力花园物业经营有限责任公司', 85, 517);
INSERT INTO `company_sorted` VALUES ('成都共享物业管理服务有限公司', 85, 518);
INSERT INTO `company_sorted` VALUES ('北京世邦魏理仕物业管理服务有限公司成都分公司', 110, 519);
INSERT INTO `company_sorted` VALUES ('成都金泉物业管理有限公司', 105, 520);
INSERT INTO `company_sorted` VALUES ('成都昊丰物业管理有限公司', 85, 521);
INSERT INTO `company_sorted` VALUES ('深圳市泰然物业管理服务有限公司成都分公司', 110, 522);
INSERT INTO `company_sorted` VALUES ('四川宏达世纪物业服务有限公司', 90, 523);
INSERT INTO `company_sorted` VALUES ('成都市梓馨物业管理有限公司', 105, 524);
INSERT INTO `company_sorted` VALUES ('成都同森物业管理有限公司', 85, 525);
INSERT INTO `company_sorted` VALUES ('成都加联圣维思物业管理有限公司', 85, 526);
INSERT INTO `company_sorted` VALUES ('四川致尚物业管理有限公司', 220, 527);
INSERT INTO `company_sorted` VALUES ('成都昌硕物业服务有限公司', 75, 528);
INSERT INTO `company_sorted` VALUES ('成都市公达物业管理有限公司', 105, 529);
INSERT INTO `company_sorted` VALUES ('成都玮盛物业服务有限公司', 135, 530);
INSERT INTO `company_sorted` VALUES ('成都倍斯特物业服务有限责任公司', 70, 531);
INSERT INTO `company_sorted` VALUES ('四川佳乐物业服务有限公司', 120, 532);
INSERT INTO `company_sorted` VALUES ('成都嘉禾物业管理有限公司', 110, 533);
INSERT INTO `company_sorted` VALUES ('双流明城物业管理有限公司', 110, 534);
INSERT INTO `company_sorted` VALUES ('四川美亚资产管理有限公司', 110, 535);
INSERT INTO `company_sorted` VALUES ('四川智诚房地产估价事务所有限责任公司', 85, 536);
INSERT INTO `company_sorted` VALUES ('成都红谷物业管理有限公司', 110, 537);
INSERT INTO `company_sorted` VALUES ('成都上达飞盛房地产经纪有限公司', 75, 538);
INSERT INTO `company_sorted` VALUES ('成都锦程物业管理有限责任公司', 85, 539);
INSERT INTO `company_sorted` VALUES ('成都台州商人置业有限公司', 85, 540);
INSERT INTO `company_sorted` VALUES ('成都胜凯物业管理有限公司', 70, 541);
INSERT INTO `company_sorted` VALUES ('四川蜀鑫投资有限公司', 90, 542);
INSERT INTO `company_sorted` VALUES ('成都兴良信房地产评估有限责任公司', 85, 543);
INSERT INTO `company_sorted` VALUES ('四川天诚物业服务有限公司', 75, 544);
INSERT INTO `company_sorted` VALUES ('成都中德红谷投资有限公司', 85, 545);
INSERT INTO `company_sorted` VALUES ('四川成功企业发展有限公司', 85, 546);
INSERT INTO `company_sorted` VALUES ('成都天府万达置业有限公司', 80, 547);
INSERT INTO `company_sorted` VALUES ('四川满城房地产经纪有限责任公司', 75, 548);
INSERT INTO `company_sorted` VALUES ('成都瑞达合能房地产有限公司', 85, 549);
INSERT INTO `company_sorted` VALUES ('成都宏洋房地产经纪有限公司', 75, 550);
INSERT INTO `company_sorted` VALUES ('成都天佳置业有限公司', 85, 551);
INSERT INTO `company_sorted` VALUES ('成都市乐城乐家市场经营管理有限责任公司', 70, 552);
INSERT INTO `company_sorted` VALUES ('成都德尚玛雅房地产经纪有限公司', 85, 553);
INSERT INTO `company_sorted` VALUES ('成都大唐依云房地产经纪有限公司', 85, 554);
INSERT INTO `company_sorted` VALUES ('简阳市九鼎房产信息服务部', 75, 555);
INSERT INTO `company_sorted` VALUES ('成都信蜀投资有限公司', 85, 556);
INSERT INTO `company_sorted` VALUES ('新都区裕信房产经纪服务部', 70, 557);
INSERT INTO `company_sorted` VALUES ('成都江合不动产经纪有限公司', 85, 558);
INSERT INTO `company_sorted` VALUES ('简阳市简城镇大昌恒房屋中介信息服务部', 75, 559);
INSERT INTO `company_sorted` VALUES ('成都昆仑房地产集团有限公司', 80, 560);
INSERT INTO `company_sorted` VALUES ('成都闲居物业管理有限公司', 110, 561);
INSERT INTO `company_sorted` VALUES ('四川辉捷物业服务有限责任公司', 110, 562);
INSERT INTO `company_sorted` VALUES ('四川诚亿物业管理有限公司', 120, 563);
INSERT INTO `company_sorted` VALUES ('成都滕王阁物业管理有限公司', 110, 564);
INSERT INTO `company_sorted` VALUES ('成都市美家美物业服务有限公司', 105, 565);
INSERT INTO `company_sorted` VALUES ('成都市金牌市场管理发展有限公司', 85, 566);
INSERT INTO `company_sorted` VALUES ('成都宏建物业管理有限公司', 75, 567);
INSERT INTO `company_sorted` VALUES ('成都市创投置业有限公司', 140, 568);
INSERT INTO `company_sorted` VALUES ('四川正源实业有限公司', 335, 569);
INSERT INTO `company_sorted` VALUES ('成都万达广场商业管理有限公司', 240, 570);
INSERT INTO `company_sorted` VALUES ('成都华兴物业管理有限公司', 110, 571);
INSERT INTO `company_sorted` VALUES ('成都华贝物业管理有限公司', 110, 572);
INSERT INTO `company_sorted` VALUES ('成都海益物业管理有限公司', 85, 573);
INSERT INTO `company_sorted` VALUES ('成都家益阳光物业管理有限公司', 85, 574);
INSERT INTO `company_sorted` VALUES ('金堂县鑫悦物业管理有限公司', 110, 575);
INSERT INTO `company_sorted` VALUES ('成都永林物业管理有限公司', 130, 576);
INSERT INTO `company_sorted` VALUES ('成都恒立物业管理有限公司', 120, 577);
INSERT INTO `company_sorted` VALUES ('四川新东原物业服务有限公司', 120, 578);
INSERT INTO `company_sorted` VALUES ('成都市捷帝置业有限公司', 90, 579);
INSERT INTO `company_sorted` VALUES ('成都盛都房地产经纪有限公司', 85, 580);
INSERT INTO `company_sorted` VALUES ('大连万象美物业管理有限公司成都分公司', 230, 581);
INSERT INTO `company_sorted` VALUES ('龙泉驿区鑫园中介服务部', 85, 582);
INSERT INTO `company_sorted` VALUES ('锦江区福铭居房屋中介咨询服务部', 90, 583);
INSERT INTO `company_sorted` VALUES ('成都万心房地产经纪有限公司', 75, 584);
INSERT INTO `company_sorted` VALUES ('简阳仁和物业管理有限公司', 70, 585);
INSERT INTO `company_sorted` VALUES ('金科物业服务有限公司成都分公司', 120, 586);
INSERT INTO `company_sorted` VALUES ('成都市高力易居物业管理有限公司', 85, 587);
INSERT INTO `company_sorted` VALUES ('中海物业管理有限公司成都中海大厦分公司', 140, 588);
INSERT INTO `company_sorted` VALUES ('四川江丰物业管理有限公司', 95, 589);
INSERT INTO `company_sorted` VALUES ('上海上房物业服务股份有限公司成都分公司', 365, 590);
INSERT INTO `company_sorted` VALUES ('北京万通鼎安国际物业服务有限公司成都分公司', 120, 591);
INSERT INTO `company_sorted` VALUES ('成都和欢物业服务有限责任公司', 120, 592);
INSERT INTO `company_sorted` VALUES ('成都全程物业服务有限公司', 85, 593);
INSERT INTO `company_sorted` VALUES ('四川省都江堰金都物业管理有限公司', 110, 594);
INSERT INTO `company_sorted` VALUES ('成都明森物业管理有限公司', 105, 595);
INSERT INTO `company_sorted` VALUES ('成都市钱江银通物业管理有限公司', 220, 596);
INSERT INTO `company_sorted` VALUES ('广西银湾物业服务有限公司成都分公司', 90, 597);
INSERT INTO `company_sorted` VALUES ('华润置地（成都）发展有限公司', 85, 598);
INSERT INTO `company_sorted` VALUES ('成都恒大新东城置业有限公司', 85, 599);
INSERT INTO `company_sorted` VALUES ('新都区大丰裕新房产信息部', 75, 600);
INSERT INTO `company_sorted` VALUES ('成都雨龙世纪置业有限公司', 80, 601);
INSERT INTO `company_sorted` VALUES ('简阳市简城镇新东方易居房地产信息服务部', 75, 602);
INSERT INTO `company_sorted` VALUES ('四川链家房地产经纪有限公司天府大道南段分公司', 85, 603);
INSERT INTO `company_sorted` VALUES ('成都顺宇物业管理有限公司', 70, 604);
INSERT INTO `company_sorted` VALUES ('成都市方圆物业管理有限公司', 85, 605);
INSERT INTO `company_sorted` VALUES ('成都市联邦信合物业管理有限责任公司', 110, 606);
INSERT INTO `company_sorted` VALUES ('成都乐当家物业管理有限公司', 105, 607);
INSERT INTO `company_sorted` VALUES ('成都世康达物业服务有限公司', 115, 608);
INSERT INTO `company_sorted` VALUES ('四川华舜物业管理有限责任公司', 140, 609);
INSERT INTO `company_sorted` VALUES ('北京中建物业管理有限公司成都分公司', 115, 610);
INSERT INTO `company_sorted` VALUES ('成都西部丽池物业发展有限公司', 120, 611);
INSERT INTO `company_sorted` VALUES ('成都科瑞福物业管理有限公司', 120, 612);
INSERT INTO `company_sorted` VALUES ('成都市鸿钰物业服务有限公司', 120, 613);
INSERT INTO `company_sorted` VALUES ('四川嘉信商运物业服务有限公司', 85, 614);
INSERT INTO `company_sorted` VALUES ('四川省鑫欧物业管理有限公司', 120, 615);
INSERT INTO `company_sorted` VALUES ('成都市鑫胜意商务服务有限公司', 110, 616);
INSERT INTO `company_sorted` VALUES ('成都市温江区成钞物业管理有限公司', 120, 617);
INSERT INTO `company_sorted` VALUES ('都江堰市嘉信屋业有限责任公司', 110, 618);
INSERT INTO `company_sorted` VALUES ('成都宏鹏物业管理有限公司', 85, 619);
INSERT INTO `company_sorted` VALUES ('成都市东兴物业管理有限公司', 150, 620);
INSERT INTO `company_sorted` VALUES ('成都腾兴物业管理服务有限公司', 105, 621);
INSERT INTO `company_sorted` VALUES ('四川省新港物业管理有限公司', 110, 622);
INSERT INTO `company_sorted` VALUES ('成都金茂物业管理有限公司', 155, 623);
INSERT INTO `company_sorted` VALUES ('四川汇德物业服务有限公司', 110, 624);
INSERT INTO `company_sorted` VALUES ('成都伯恩物业管理有限公司', 110, 625);
INSERT INTO `company_sorted` VALUES ('北京市均豪物业管理股份有限公司成都分公司', 85, 626);
INSERT INTO `company_sorted` VALUES ('成都市捷达物业管理有限责任公司', 105, 627);
INSERT INTO `company_sorted` VALUES ('成都安怡物业管理有限公司', 120, 628);
INSERT INTO `company_sorted` VALUES ('成都市新都民生物业管理有限公司', 105, 629);
INSERT INTO `company_sorted` VALUES ('成都科奥达物业管理有限责任公司', 115, 630);
INSERT INTO `company_sorted` VALUES ('成都前方物业服务有限公司', 85, 631);
INSERT INTO `company_sorted` VALUES ('四川丽龙房地产开发有限公司', 80, 632);
INSERT INTO `company_sorted` VALUES ('成都玛雅御征房地产经纪有限公司', 75, 633);
INSERT INTO `company_sorted` VALUES ('成都卓信合创房地产经纪有限公司', 85, 634);
INSERT INTO `company_sorted` VALUES ('成都丰伟房地产经纪有限公司', 70, 635);
INSERT INTO `company_sorted` VALUES ('成都西都易城房地产经纪有限公司玺龙湾店', 85, 636);

-- ----------------------------
-- Table structure for economic_active
-- ----------------------------
DROP TABLE IF EXISTS `economic_active`;
CREATE TABLE `economic_active`  (
  `city` text CHARACTER SET utf8 COLLATE utf8_bin,
  `count` bigint(20) DEFAULT NULL,
  `price` double DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of economic_active
-- ----------------------------
INSERT INTO `economic_active` VALUES ('海口', 621, 16806.334943639293, 1);
INSERT INTO `economic_active` VALUES ('长沙', 979, 12657.391215526048, 2);
INSERT INTO `economic_active` VALUES ('兰州', 1153, 13161.078924544667, 3);
INSERT INTO `economic_active` VALUES ('哈尔滨', 1396, 10843.722779369627, 4);
INSERT INTO `economic_active` VALUES ('南宁', 1506, 13470.575697211156, 5);
INSERT INTO `economic_active` VALUES ('银川', 1937, 5570.401652039236, 6);
INSERT INTO `economic_active` VALUES ('呼和浩特', 2097, 11637.122079160707, 7);
INSERT INTO `economic_active` VALUES ('昆明', 2786, 13716.854630294329, 8);
INSERT INTO `economic_active` VALUES ('贵阳', 2829, 11281.103923647932, 9);
INSERT INTO `economic_active` VALUES ('南昌', 2954, 16813.833107650644, 10);

-- ----------------------------
-- Table structure for every_regions_ershoufang_count
-- ----------------------------
DROP TABLE IF EXISTS `every_regions_ershoufang_count`;
CREATE TABLE `every_regions_ershoufang_count`  (
  `city` text CHARACTER SET utf8 COLLATE utf8_bin,
  `count` bigint(20) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of every_regions_ershoufang_count
-- ----------------------------
INSERT INTO `every_regions_ershoufang_count` VALUES ('华东', 114564, 1);
INSERT INTO `every_regions_ershoufang_count` VALUES ('西南', 60525, 2);
INSERT INTO `every_regions_ershoufang_count` VALUES ('华南', 20114, 3);
INSERT INTO `every_regions_ershoufang_count` VALUES ('西北', 1153, 4);
INSERT INTO `every_regions_ershoufang_count` VALUES ('华北', 77690, 5);
INSERT INTO `every_regions_ershoufang_count` VALUES ('华中', 47189, 6);
INSERT INTO `every_regions_ershoufang_count` VALUES ('东北', 24692, 7);

-- ----------------------------
-- Table structure for every_regions_zufang_count
-- ----------------------------
DROP TABLE IF EXISTS `every_regions_zufang_count`;
CREATE TABLE `every_regions_zufang_count`  (
  `city` text CHARACTER SET utf8 COLLATE utf8_bin,
  `count` bigint(20) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of every_regions_zufang_count
-- ----------------------------
INSERT INTO `every_regions_zufang_count` VALUES ('华北', 84002, 1);
INSERT INTO `every_regions_zufang_count` VALUES ('华中', 81424, 2);
INSERT INTO `every_regions_zufang_count` VALUES ('东北', 56673, 3);
INSERT INTO `every_regions_zufang_count` VALUES ('华东', 152438, 4);
INSERT INTO `every_regions_zufang_count` VALUES ('西南', 105814, 5);
INSERT INTO `every_regions_zufang_count` VALUES ('华南', 36039, 6);
INSERT INTO `every_regions_zufang_count` VALUES ('西北', 6569, 7);

-- ----------------------------
-- Table structure for fang_wu_zheng_shou
-- ----------------------------
DROP TABLE IF EXISTS `fang_wu_zheng_shou`;
CREATE TABLE `fang_wu_zheng_shou`  (
  `area` text CHARACTER SET utf8 COLLATE utf8_bin,
  `counter` bigint(20) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fang_wu_zheng_shou
-- ----------------------------
INSERT INTO `fang_wu_zheng_shou` VALUES ('龙泉驿区', 9, 1);
INSERT INTO `fang_wu_zheng_shou` VALUES ('金堂县', 10, 2);
INSERT INTO `fang_wu_zheng_shou` VALUES ('邛崃市', 10, 3);
INSERT INTO `fang_wu_zheng_shou` VALUES ('简阳市', 5, 4);
INSERT INTO `fang_wu_zheng_shou` VALUES ('锦江', 2, 5);
INSERT INTO `fang_wu_zheng_shou` VALUES ('金牛区', 26, 6);
INSERT INTO `fang_wu_zheng_shou` VALUES ('天府新区', 3, 7);
INSERT INTO `fang_wu_zheng_shou` VALUES ('武侯区', 43, 8);
INSERT INTO `fang_wu_zheng_shou` VALUES ('新津县', 16, 9);
INSERT INTO `fang_wu_zheng_shou` VALUES ('彭州市', 2, 10);
INSERT INTO `fang_wu_zheng_shou` VALUES ('锦江区', 43, 11);
INSERT INTO `fang_wu_zheng_shou` VALUES ('成华区', 178, 12);
INSERT INTO `fang_wu_zheng_shou` VALUES ('双流区', 2, 13);
INSERT INTO `fang_wu_zheng_shou` VALUES ('崇州市', 10, 14);
INSERT INTO `fang_wu_zheng_shou` VALUES ('高新区', 31, 15);
INSERT INTO `fang_wu_zheng_shou` VALUES ('青白江区', 13, 16);
INSERT INTO `fang_wu_zheng_shou` VALUES ('温江区', 7, 17);
INSERT INTO `fang_wu_zheng_shou` VALUES ('都江堰市', 52, 18);
INSERT INTO `fang_wu_zheng_shou` VALUES ('大邑县', 1, 19);
INSERT INTO `fang_wu_zheng_shou` VALUES ('郫都区', 1, 20);
INSERT INTO `fang_wu_zheng_shou` VALUES ('青羊区', 37, 21);

-- ----------------------------
-- Table structure for gong_zu_fang
-- ----------------------------
DROP TABLE IF EXISTS `gong_zu_fang`;
CREATE TABLE `gong_zu_fang`  (
  `area` double DEFAULT NULL,
  `counter` bigint(20) DEFAULT NULL,
  `location` text CHARACTER SET utf8 COLLATE utf8_bin,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of gong_zu_fang
-- ----------------------------
INSERT INTO `gong_zu_fang` VALUES (51.96032038834959, 2060, '金牛区', 1);
INSERT INTO `gong_zu_fang` VALUES (52.51285436893205, 515, '高新区', 2);
INSERT INTO `gong_zu_fang` VALUES (52.35300423131179, 2127, '青羊区', 3);
INSERT INTO `gong_zu_fang` VALUES (52.31904802021897, 2374, '锦江区', 4);
INSERT INTO `gong_zu_fang` VALUES (52.28998003992027, 1503, '成华区', 5);
INSERT INTO `gong_zu_fang` VALUES (52.419591836734746, 1421, '武侯区', 6);

-- ----------------------------
-- Table structure for serven_area
-- ----------------------------
DROP TABLE IF EXISTS `serven_area`;
CREATE TABLE `serven_area`  (
  `city` text CHARACTER SET utf8 COLLATE utf8_bin,
  `price` double DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of serven_area
-- ----------------------------
INSERT INTO `serven_area` VALUES ('华北', 36587.16856738319, 1);
INSERT INTO `serven_area` VALUES ('华中', 17037.053084405263, 3);
INSERT INTO `serven_area` VALUES ('东北', 13974.650575085048, 4);
INSERT INTO `serven_area` VALUES ('华东', 34989.704977130685, 5);
INSERT INTO `serven_area` VALUES ('西南', 14859.51102850062, 6);
INSERT INTO `serven_area` VALUES ('华南', 35688.45117828378, 7);
INSERT INTO `serven_area` VALUES ('西北', 13161.078924544667, 8);

-- ----------------------------
-- Table structure for yu_shou_trend
-- ----------------------------
DROP TABLE IF EXISTS `yu_shou_trend`;
CREATE TABLE `yu_shou_trend`  (
  `area` double DEFAULT NULL,
  `year` text CHARACTER SET utf8 COLLATE utf8_bin,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of yu_shou_trend
-- ----------------------------
INSERT INTO `yu_shou_trend` VALUES (73565.7099999986, '2001', 1);
INSERT INTO `yu_shou_trend` VALUES (96788.7100000004, '2000', 2);
INSERT INTO `yu_shou_trend` VALUES (428679.599999994, '2005', 3);
INSERT INTO `yu_shou_trend` VALUES (664190.529999994, '2006', 4);
INSERT INTO `yu_shou_trend` VALUES (107877.379999999, '2008', 5);
INSERT INTO `yu_shou_trend` VALUES (642765.869999995, '2009', 6);
INSERT INTO `yu_shou_trend` VALUES (340600.5, '1996', 7);
INSERT INTO `yu_shou_trend` VALUES (721166.5800000001, '1997', 8);
INSERT INTO `yu_shou_trend` VALUES (996555.3, '1998', 9);
INSERT INTO `yu_shou_trend` VALUES (1996912.51, '2018', 10);
INSERT INTO `yu_shou_trend` VALUES (212821.9699999997, '1999', 11);
INSERT INTO `yu_shou_trend` VALUES (983828.890000008, '2011', 12);
INSERT INTO `yu_shou_trend` VALUES (67046.749999999, '2004', 13);
INSERT INTO `yu_shou_trend` VALUES (2811084.5200003, '2002', 14);
INSERT INTO `yu_shou_trend` VALUES (195898.280000002, '2003', 15);
INSERT INTO `yu_shou_trend` VALUES (874236.289999995, '2007', 16);
INSERT INTO `yu_shou_trend` VALUES (175134, '1994', 17);
INSERT INTO `yu_shou_trend` VALUES (352863, '1995', 18);
INSERT INTO `yu_shou_trend` VALUES (797033.80000002, '2010', 19);
INSERT INTO `yu_shou_trend` VALUES (488778.56000001, '2012', 20);
INSERT INTO `yu_shou_trend` VALUES (264786.170000006, '2013', 21);
INSERT INTO `yu_shou_trend` VALUES (574382.54999999, '2014', 22);
INSERT INTO `yu_shou_trend` VALUES (890326.41, '2015', 23);
INSERT INTO `yu_shou_trend` VALUES (915566.229999999, '2016', 24);
INSERT INTO `yu_shou_trend` VALUES (670265.519999999, '2017', 25);
INSERT INTO `yu_shou_trend` VALUES (7368, '1901', 26);

-- ----------------------------
-- Table structure for zufang_shoufang_price_compare
-- ----------------------------
DROP TABLE IF EXISTS `zufang_shoufang_price_compare`;
CREATE TABLE `zufang_shoufang_price_compare`  (
  `city` text CHARACTER SET utf8 COLLATE utf8_bin,
  `data_type` text CHARACTER SET utf8 COLLATE utf8_bin,
  `price` double DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of zufang_shoufang_price_compare
-- ----------------------------
INSERT INTO `zufang_shoufang_price_compare` VALUES ('华北', 'ershoufang', 36587.16856738319, 1);
INSERT INTO `zufang_shoufang_price_compare` VALUES ('华中', 'ershoufang', 17037.053084405263, 3);
INSERT INTO `zufang_shoufang_price_compare` VALUES ('东北', 'ershoufang', 13974.650575085048, 4);
INSERT INTO `zufang_shoufang_price_compare` VALUES ('华北', 'zufang', 4131.815944858456, 5);
INSERT INTO `zufang_shoufang_price_compare` VALUES ('华中', 'zufang', 2599.3494792690117, 7);
INSERT INTO `zufang_shoufang_price_compare` VALUES ('东北', 'zufang', 2799.5014733647417, 8);
INSERT INTO `zufang_shoufang_price_compare` VALUES ('华东', 'ershoufang', 34989.704977130685, 9);
INSERT INTO `zufang_shoufang_price_compare` VALUES ('西南', 'ershoufang', 14859.51102850062, 10);
INSERT INTO `zufang_shoufang_price_compare` VALUES ('华南', 'ershoufang', 35688.45117828378, 11);
INSERT INTO `zufang_shoufang_price_compare` VALUES ('西北', 'ershoufang', 13161.078924544667, 12);
INSERT INTO `zufang_shoufang_price_compare` VALUES ('华东', 'zufang', 4468.232934045317, 13);
INSERT INTO `zufang_shoufang_price_compare` VALUES ('西南', 'zufang', 2447.541478443306, 14);
INSERT INTO `zufang_shoufang_price_compare` VALUES ('华南', 'zufang', 3082.847942506729, 15);
INSERT INTO `zufang_shoufang_price_compare` VALUES ('西北', 'zufang', 2868.112193636779, 16);

SET FOREIGN_KEY_CHECKS = 1;
