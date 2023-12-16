/*
 Navicat Premium Data Transfer

 Source Server         : MySQL57
 Source Server Type    : MySQL
 Source Server Version : 50744
 Source Host           : localhost:3306
 Source Schema         : alocation

 Target Server Type    : MySQL
 Target Server Version : 50744
 File Encoding         : 65001

 Date: 12/12/2023 01:11:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for area_data
-- ----------------------------
DROP TABLE IF EXISTS `area_data`;
CREATE TABLE `area_data`  (
  `area_id` int(255) UNSIGNED ZEROFILL NOT NULL,
  `area_locations` json NOT NULL,
  `area_date` int(255) NOT NULL,
  `area_info` json NULL,
  `area_pois` json NULL,
  `area_extend` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`area_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of area_data
-- ----------------------------

-- ----------------------------
-- Table structure for comment_data
-- ----------------------------
DROP TABLE IF EXISTS `comment_data`;
CREATE TABLE `comment_data`  (
  `comment_id` int(10) UNSIGNED ZEROFILL NOT NULL,
  `owner` int(10) UNSIGNED NOT NULL,
  `pois_id` int(10) UNSIGNED NOT NULL,
  `root` int(10) UNSIGNED NOT NULL,
  `parent` int(10) UNSIGNED NOT NULL,
  `commentContent` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `date` int(10) UNSIGNED NOT NULL,
  `commentLevel` int(10) UNSIGNED NOT NULL,
  `type` int(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`comment_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of comment_data
-- ----------------------------

-- ----------------------------
-- Table structure for feedback_data
-- ----------------------------
DROP TABLE IF EXISTS `feedback_data`;
CREATE TABLE `feedback_data`  (
  `feedback_id` int(11) NOT NULL,
  `feedback_info` json NOT NULL,
  `feedback_type` int(11) NOT NULL,
  `feedback_date` int(11) NOT NULL,
  `feedback_images` json NULL,
  `feedback_owenr` int(11) NOT NULL,
  `feedback_solution` json NULL,
  `feedback_solved_date` int(11) NULL DEFAULT NULL,
  `feedback_extend` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`feedback_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of feedback_data
-- ----------------------------

-- ----------------------------
-- Table structure for pois_data
-- ----------------------------
DROP TABLE IF EXISTS `pois_data`;
CREATE TABLE `pois_data`  (
  `poi_id` int(255) NOT NULL,
  `poi_info` json NULL,
  `poi_owenr` int(255) NOT NULL,
  `poi_location` json NOT NULL,
  `poi_date` int(255) NOT NULL,
  `poi_star` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `poi_comments` json NULL,
  `poi_share` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `poi_pv` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `poi_uv` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `poi_images` json NULL,
  `poi_extend` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`poi_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of pois_data
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `user_account` int(255) UNSIGNED ZEROFILL NOT NULL COMMENT '用户id',
  `user_phone` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_real_info` json NOT NULL,
  `user_real_status` tinyint(1) NOT NULL,
  `user_qr_code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_privilege` int(16) NOT NULL,
  `user_extend` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`user_account`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------

-- ----------------------------
-- Table structure for user_data
-- ----------------------------
DROP TABLE IF EXISTS `user_data`;
CREATE TABLE `user_data`  (
  `user_account` int(255) UNSIGNED ZEROFILL NOT NULL COMMENT '用户id',
  `user_avatar` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_bg` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_info` json NULL,
  `user_pois` json NULL,
  `user_history` json NULL,
  `user_footprint` json NULL,
  `user_favorites` json NULL,
  `user_follow` json NULL,
  `user_followed` json NULL,
  `user_extend` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`user_account`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_data
-- ----------------------------

-- ----------------------------
-- Table structure for user_tag
-- ----------------------------
DROP TABLE IF EXISTS `user_tag`;
CREATE TABLE `user_tag`  (
  `tag_id` int(10) UNSIGNED ZEROFILL NOT NULL,
  `tag_content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tag_heat` int(10) UNSIGNED ZEROFILL NOT NULL,
  PRIMARY KEY (`tag_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_tag
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
