-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Nov 04, 2015 at 05:18 PM
-- Server version: 5.6.20
-- PHP Version: 5.5.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";
CREATE DATABASE IF NOT EXISTS `conve` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `conve`;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `conve`
--

-- --------------------------------------------------------

--
-- Table structure for table `accountmanagement_account`
--

CREATE TABLE IF NOT EXISTS `accountmanagement_account` (
`id` int(11) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `address` longtext,
  `created_date` datetime NOT NULL,
  `description` longtext,
  `email` varchar(254),
  `facebook_link` varchar(200),
  `phone` varchar(50),
  `photo_link` longtext,
  `user_id` int(11) DEFAULT NULL,
  `view_num` int(11) NOT NULL,
  `extra_phone` varchar(50) DEFAULT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `accountmanagement_account`
--

INSERT INTO `accountmanagement_account` (`id`, `last_name`, `first_name`, `address`, `created_date`, `description`, `email`, `facebook_link`, `phone`, `photo_link`, `user_id`, `view_num`, `extra_phone`) VALUES
(10, 'default', 'dan', 'Blk 32 Paya Lebar', '2015-10-30 18:08:20', NULL, 'nick@gmail.com', 'https://www.facebook.com/KennySang/?fref=ts', '85368689', NULL, 18, 0, '+84 55687547579');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
`id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
`id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
`id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=34 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add record', 7, 'add_record'),
(20, 'Can change record', 7, 'change_record'),
(21, 'Can delete record', 7, 'delete_record'),
(22, 'Can add email', 8, 'add_email'),
(23, 'Can change email', 8, 'change_email'),
(24, 'Can delete email', 8, 'delete_email'),
(25, 'Can add account', 9, 'add_account'),
(26, 'Can change account', 9, 'change_account'),
(27, 'Can delete account', 9, 'delete_account'),
(28, 'Can add request', 10, 'add_request'),
(29, 'Can change request', 10, 'change_request'),
(30, 'Can delete request', 10, 'delete_request'),
(31, 'Can add chat', 11, 'add_chat'),
(32, 'Can change chat', 11, 'change_chat'),
(33, 'Can delete chat', 11, 'delete_chat');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
`id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=19 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(18, 'pbkdf2_sha256$20000$tBa7SM4ZKPYQ$ahOPGvhzNv88wHLpDkazyAyrUfcnqd7kOPOkiWXER8k=', '2015-11-02 15:37:22', 0, 'dan', '', '', '', 0, 1, '2015-10-30 18:09:55');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
`id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
`id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
`id` int(11) NOT NULL,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
`id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(9, 'AccountManagement', 'account'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(8, 'LandingPage', 'email'),
(7, 'LandingPage', 'record'),
(11, 'RequestManagement', 'chat'),
(10, 'RequestManagement', 'request'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
`id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=29 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2015-10-22 17:29:25'),
(2, 'auth', '0001_initial', '2015-10-22 17:29:35'),
(3, 'AccountManagement', '0001_initial', '2015-10-22 17:29:35'),
(4, 'AccountManagement', '0002_auto_20151022_2313', '2015-10-22 17:29:44'),
(5, 'AccountManagement', '0003_auto_20151022_2314', '2015-10-22 17:29:44'),
(6, 'AccountManagement', '0004_auto_20151022_2316', '2015-10-22 17:29:44'),
(7, 'AccountManagement', '0005_auto_20151023_0129', '2015-10-22 17:29:45'),
(8, 'LandingPage', '0001_initial', '2015-10-22 17:29:46'),
(9, 'LandingPage', '0002_record', '2015-10-22 17:29:46'),
(10, 'RequestManagement', '0001_initial', '2015-10-22 17:29:54'),
(11, 'admin', '0001_initial', '2015-10-22 17:29:56'),
(12, 'contenttypes', '0002_remove_content_type_name', '2015-10-22 17:29:57'),
(13, 'auth', '0002_alter_permission_name_max_length', '2015-10-22 17:29:59'),
(14, 'auth', '0003_alter_user_email_max_length', '2015-10-22 17:30:00'),
(15, 'auth', '0004_alter_user_username_opts', '2015-10-22 17:30:00'),
(16, 'auth', '0005_alter_user_last_login_null', '2015-10-22 17:30:00'),
(17, 'auth', '0006_require_contenttypes_0002', '2015-10-22 17:30:00'),
(18, 'sessions', '0001_initial', '2015-10-22 17:30:01'),
(19, 'AccountManagement', '0006_auto_20151027_2320', '2015-10-27 15:20:30'),
(20, 'RequestManagement', '0002_auto_20151027_2320', '2015-10-27 15:20:33'),
(21, 'AccountManagement', '0007_auto_20151030_2354', '2015-10-30 15:54:56'),
(22, 'RequestManagement', '0003_auto_20151030_2354', '2015-10-30 15:54:57'),
(23, 'AccountManagement', '0008_auto_20151103_0123', '2015-11-02 17:23:36'),
(24, 'RequestManagement', '0004_auto_20151103_0123', '2015-11-02 17:23:36'),
(25, 'AccountManagement', '0009_auto_20151105_0005', '2015-11-04 16:05:48'),
(26, 'RequestManagement', '0005_auto_20151105_0005', '2015-11-04 16:05:48'),
(27, 'AccountManagement', '0010_auto_20151105_0017', '2015-11-04 16:17:28'),
(28, 'RequestManagement', '0006_auto_20151105_0017', '2015-11-04 16:17:28');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('18skvw4m5d8u8kf90duhmxe3o63bpf2u', 'OTQxYmI3NGE3YWQ5YTk4NDYxOTRlM2QxZmUyNWJmNDA4YWJhYjU4Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlZTc3NmUyNDFjMDlhMTkyZmE5OTI2Mjg5ODc2NTA0NWQ5M2QxYmEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9', '2015-11-14 14:04:03'),
('85l9sejhwkauon1x9jx3ipeluwx0yg25', 'OTQxYmI3NGE3YWQ5YTk4NDYxOTRlM2QxZmUyNWJmNDA4YWJhYjU4Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlZTc3NmUyNDFjMDlhMTkyZmE5OTI2Mjg5ODc2NTA0NWQ5M2QxYmEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9', '2015-11-14 14:16:35'),
('8ec5z8vg9maqextbybdhxoi6z3jnbxo1', 'OTQxYmI3NGE3YWQ5YTk4NDYxOTRlM2QxZmUyNWJmNDA4YWJhYjU4Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlZTc3NmUyNDFjMDlhMTkyZmE5OTI2Mjg5ODc2NTA0NWQ5M2QxYmEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9', '2015-11-14 14:05:58'),
('a9153ldsvt5ykym00lo6mk3yay7c9o9q', 'OTQxYmI3NGE3YWQ5YTk4NDYxOTRlM2QxZmUyNWJmNDA4YWJhYjU4Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlZTc3NmUyNDFjMDlhMTkyZmE5OTI2Mjg5ODc2NTA0NWQ5M2QxYmEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9', '2015-11-14 14:17:14'),
('cboldrf10wu7d677009vnalacw5gz1r2', 'OTQxYmI3NGE3YWQ5YTk4NDYxOTRlM2QxZmUyNWJmNDA4YWJhYjU4Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlZTc3NmUyNDFjMDlhMTkyZmE5OTI2Mjg5ODc2NTA0NWQ5M2QxYmEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9', '2015-11-14 14:23:46'),
('fjesgmhwq1w6xhe2l8eygc2jaivqyu4b', 'OTQxYmI3NGE3YWQ5YTk4NDYxOTRlM2QxZmUyNWJmNDA4YWJhYjU4Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlZTc3NmUyNDFjMDlhMTkyZmE5OTI2Mjg5ODc2NTA0NWQ5M2QxYmEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9', '2015-11-14 13:49:48'),
('htu60f4s8hl77yyhpe4nvbp3p6rhityx', 'OTQxYmI3NGE3YWQ5YTk4NDYxOTRlM2QxZmUyNWJmNDA4YWJhYjU4Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlZTc3NmUyNDFjMDlhMTkyZmE5OTI2Mjg5ODc2NTA0NWQ5M2QxYmEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9', '2015-11-14 14:21:33'),
('jbi73wnez67bk08sa76k6yq8n7zrv00x', 'OTQxYmI3NGE3YWQ5YTk4NDYxOTRlM2QxZmUyNWJmNDA4YWJhYjU4Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlZTc3NmUyNDFjMDlhMTkyZmE5OTI2Mjg5ODc2NTA0NWQ5M2QxYmEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9', '2015-11-16 15:37:22'),
('l4r8nqjlkko7g2go5g4gxoura8rcv5cn', 'OTQxYmI3NGE3YWQ5YTk4NDYxOTRlM2QxZmUyNWJmNDA4YWJhYjU4Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlZTc3NmUyNDFjMDlhMTkyZmE5OTI2Mjg5ODc2NTA0NWQ5M2QxYmEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9', '2015-11-14 13:44:38'),
('n51h5huryuezb3xkxrcfebgms78rztd4', 'OTQxYmI3NGE3YWQ5YTk4NDYxOTRlM2QxZmUyNWJmNDA4YWJhYjU4Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlZTc3NmUyNDFjMDlhMTkyZmE5OTI2Mjg5ODc2NTA0NWQ5M2QxYmEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9', '2015-11-14 13:49:18'),
('om3ib0z6fhf7qhugxu7zollqn6icc9fp', 'OTQxYmI3NGE3YWQ5YTk4NDYxOTRlM2QxZmUyNWJmNDA4YWJhYjU4Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlZTc3NmUyNDFjMDlhMTkyZmE5OTI2Mjg5ODc2NTA0NWQ5M2QxYmEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9', '2015-11-14 14:17:49'),
('vf8y12tgs0ejm4yyvv1byhs6p515vmwl', 'OTQxYmI3NGE3YWQ5YTk4NDYxOTRlM2QxZmUyNWJmNDA4YWJhYjU4Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlZTc3NmUyNDFjMDlhMTkyZmE5OTI2Mjg5ODc2NTA0NWQ5M2QxYmEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9', '2015-11-14 14:27:22'),
('x5k8tpt95fde776dbrr3rjm0p2owkags', 'OTQxYmI3NGE3YWQ5YTk4NDYxOTRlM2QxZmUyNWJmNDA4YWJhYjU4Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlZTc3NmUyNDFjMDlhMTkyZmE5OTI2Mjg5ODc2NTA0NWQ5M2QxYmEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9', '2015-11-14 13:45:22'),
('yoszn2j8ict2cvf9otxc5ypxx48z1t36', 'OTQxYmI3NGE3YWQ5YTk4NDYxOTRlM2QxZmUyNWJmNDA4YWJhYjU4Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjBlZTc3NmUyNDFjMDlhMTkyZmE5OTI2Mjg5ODc2NTA0NWQ5M2QxYmEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxOCJ9', '2015-11-14 14:15:42');

-- --------------------------------------------------------

--
-- Table structure for table `landingpage_email`
--

CREATE TABLE IF NOT EXISTS `landingpage_email` (
`id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `landingpage_record`
--

CREATE TABLE IF NOT EXISTS `landingpage_record` (
`id` int(11) NOT NULL,
  `direction` varchar(50) NOT NULL,
  `shipper_name` varchar(50) NOT NULL,
  `kg_available` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `price` varchar(200) DEFAULT NULL,
  `contact` varchar(200) DEFAULT NULL,
  `pick_up_destination` varchar(100) DEFAULT NULL,
  `release_destination` varchar(100) DEFAULT NULL,
  `note` varchar(1000) DEFAULT NULL,
  `url` longtext,
  `code` varchar(50) DEFAULT NULL,
  `is_checked` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `requestmanagement_chat`
--

CREATE TABLE IF NOT EXISTS `requestmanagement_chat` (
`id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `description` longtext,
  `listen_account_id` int(11) NOT NULL,
  `request_id` int(11) NOT NULL,
  `speak_account_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `requestmanagement_request`
--

CREATE TABLE IF NOT EXISTS `requestmanagement_request` (
`id` int(11) NOT NULL,
  `title` longtext NOT NULL,
  `description` longtext,
  `category` varchar(50),
  `price` varchar(50) DEFAULT NULL,
  `status` varchar(50) NOT NULL,
  `created_date` datetime NOT NULL,
  `closed_date` datetime DEFAULT NULL,
  `expired_date` datetime DEFAULT NULL,
  `origin_city` varchar(225) DEFAULT NULL,
  `origin_address` longtext,
  `destination_city` varchar(225) NOT NULL,
  `destination_address` longtext,
  `view_num` int(11) NOT NULL,
  `image_url` longtext,
  `account_id` int(11) NOT NULL,
  `asap` tinyint(1) NOT NULL,
  `last_modified_date` datetime DEFAULT NULL,
  `thumb_url` longtext
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `requestmanagement_request`
--

INSERT INTO `requestmanagement_request` (`id`, `title`, `description`, `category`, `price`, `status`, `created_date`, `closed_date`, `expired_date`, `origin_city`, `origin_address`, `destination_city`, `destination_address`, `view_num`, `image_url`, `account_id`, `asap`, `last_modified_date`, `thumb_url`) VALUES
(17, 'Chuy?n iphone', '?? ?n', '1', '1', '1', '2015-11-02 17:46:41', NULL, NULL, '1', 'Jurong East', '3', 'ph? c?', 0, '', 10, 1, NULL, NULL),
(18, 'sfsda', 'afsdfa', '2', '23', '1', '2015-11-02 17:46:41', NULL, NULL, '1', 'sfasd', '3', 'asfa', 0, '', 10, 1, NULL, NULL),
(19, 'sfas', 'asfsdfa', '3;2', '100', '2', '2015-11-02 17:46:41', '2015-11-03 00:00:00', NULL, '3', 'sfas', '1', 'afsdf', 0, '', 10, 1, NULL, NULL),
(21, 'dsfds', 'sdfsd', ';1;2', '5', '1', '2015-11-04 15:07:53', NULL, NULL, '3', 'sdfds', '1', 'sfdsd', 0, '', 10, 1, NULL, NULL),
(22, 'sadsa', 'asda', ';1;2', '5', '1', '2015-11-04 15:26:48', NULL, NULL, '3', 'asdas', '1', 'asdas', 0, '', 10, 1, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accountmanagement_account`
--
ALTER TABLE `accountmanagement_account`
 ADD PRIMARY KEY (`id`), ADD KEY `AccountManagement_account_e8701ad4` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `group_id` (`group_id`,`permission_id`), ADD KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `content_type_id` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `user_id` (`user_id`,`group_id`), ADD KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `user_id` (`user_id`,`permission_id`), ADD KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
 ADD PRIMARY KEY (`id`), ADD KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`), ADD KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
 ADD PRIMARY KEY (`session_key`), ADD KEY `django_session_de54fa62` (`expire_date`);

--
-- Indexes for table `landingpage_email`
--
ALTER TABLE `landingpage_email`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `landingpage_record`
--
ALTER TABLE `landingpage_record`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `code` (`code`);

--
-- Indexes for table `requestmanagement_chat`
--
ALTER TABLE `requestmanagement_chat`
 ADD PRIMARY KEY (`id`), ADD KEY `Reque_listen_account_id_4e99b284_fk_AccountManagement_account_id` (`listen_account_id`), ADD KEY `RequestManagement_chat_f68d2c36` (`request_id`), ADD KEY `RequestManagement_chat_6f1c87a1` (`speak_account_id`);

--
-- Indexes for table `requestmanagement_request`
--
ALTER TABLE `requestmanagement_request`
 ADD PRIMARY KEY (`id`), ADD KEY `RequestManag_account_id_507b65b1_fk_AccountManagement_account_id` (`account_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accountmanagement_account`
--
ALTER TABLE `accountmanagement_account`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=34;
--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=19;
--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=29;
--
-- AUTO_INCREMENT for table `landingpage_email`
--
ALTER TABLE `landingpage_email`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `landingpage_record`
--
ALTER TABLE `landingpage_record`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `requestmanagement_chat`
--
ALTER TABLE `requestmanagement_chat`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `requestmanagement_request`
--
ALTER TABLE `requestmanagement_request`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=23;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `accountmanagement_account`
--
ALTER TABLE `accountmanagement_account`
ADD CONSTRAINT `AccountManagement_account_user_id_7cf51676_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
ADD CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
ADD CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
ADD CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
ADD CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
ADD CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
ADD CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
ADD CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
ADD CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
ADD CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `requestmanagement_chat`
--
ALTER TABLE `requestmanagement_chat`
ADD CONSTRAINT `Reque_listen_account_id_4e99b284_fk_AccountManagement_account_id` FOREIGN KEY (`listen_account_id`) REFERENCES `accountmanagement_account` (`id`),
ADD CONSTRAINT `Reques_speak_account_id_3d553264_fk_AccountManagement_account_id` FOREIGN KEY (`speak_account_id`) REFERENCES `accountmanagement_account` (`id`),
ADD CONSTRAINT `RequestManag_request_id_4b3f4b5b_fk_RequestManagement_request_id` FOREIGN KEY (`request_id`) REFERENCES `requestmanagement_request` (`id`);

--
-- Constraints for table `requestmanagement_request`
--
ALTER TABLE `requestmanagement_request`
ADD CONSTRAINT `RequestManag_account_id_507b65b1_fk_AccountManagement_account_id` FOREIGN KEY (`account_id`) REFERENCES `accountmanagement_account` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
