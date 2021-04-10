import time
import unittest

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class DataReplay(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.p = pwd()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_to_adminconsole(self.driver)
        self.data.click_data_replay(self.driver)
        time.sleep(2)

    def test_data_replay_icon(self):
        self.assertIn("data-replay",self.driver.current_url,"Data-replay icon is not working")

    def test_data_replay_hamburger_menu_icon(self):
        self.data.click_on_home()
        self.data.click_humburger_menu()
        self.data.click_humburger_data_replay_icon()
        self.assertIn("data-replay", self.driver.current_url, "Data-replay hamburger icon is not working")

    def test_without_selecting_data_source(self):
        self.data.click_data_replay_submit_button(self.driver)
        self.data.click_ok_on_alertbox(self.driver)
        self.assertIn("data-replay", self.driver.current_url, "Data-replay alert is not working")

    def test_select_data_source_is_dispalyed_on_select_box(self):
        message = self.data.check_data_source_message_on_select_box()
        self.assertEqual(message.text, "Select Data Source", "select data source is not selected from select box by default")



    def test_data_replay_crc(self):
        self.data.select_data_replay_data_source(self.driver, "CRC")
        time.sleep(2)
        year = self.data.get_crc_year()
        self.data.select_data_replay_year(self.driver, year)
        time.sleep(2)
        multi_select_button = self.data.click_multi_select_button()
        multi_select_button.click()
        choose_first_option = self.data.select_multi_option_button()
        choose_first_option.click()
        month = choose_first_option.text
        month = self.data.get_crc_month(month)
        #self.data.click_data_replay_submit_button(self.driver)
        time.sleep(5)
        #self.data.click_ok_on_alertbox(self.driver)
        crc_location_trans = self.data.get_table_data_count(
            "crc_location_trans where year = {} and month = {}".format(year, month))
        crc_inspection_trans = self.data.get_table_data_count(
            "crc_inspection_trans where year = {} and month = {}".format(year, month))
        crc_visits_frequency = self.data.get_table_data_count(
            "crc_visits_frequency where year = {} and month = {}".format(year, month))


        with self.subTest():
            self.assertEqual(crc_location_trans, 0, "crc_location_trans data is not deleted")
        with self.subTest():
            self.assertEqual(crc_inspection_trans, 0, "crc_inspection_trans data is not deleted")
        with self.subTest():
            self.assertEqual(crc_visits_frequency, 0, "crc_visits_frequency data is not deleted")


    def test_data_replay_infrastructure(self):
        self.data.select_data_replay_data_source(self.driver,"Infrastructure")
        time.sleep(2)
        self.data.select_data_replay_year(self.driver, " Delete all data")
        self.data.click_data_replay_submit_button(self.driver)
        time.sleep(5)
        self.data.click_ok_on_alertbox(self.driver)
        infrastructure_temp = self.data.get_table_data_count("infrastructure_temp")
        infrastructure_trans = self.data.get_table_data_count("infrastructure_trans")
        with self.subTest():
            self.assertEqual(infrastructure_temp, 0, "infrastructure_temp data is not deleted")
        with self.subTest():
            self.assertEqual(infrastructure_trans, 0, "infrastructure_trans data is not deleted")

    def test_data_replay_static(self):
        self.data.select_data_replay_data_source(self.driver, "Static")
        time.sleep(2)
        self.data.select_data_replay_year(self.driver, " Delete all data")
        time.sleep(2)
        self.data.click_data_replay_submit_button(self.driver)
        time.sleep(5)
        self.data.click_ok_on_alertbox(self.driver)
        district_tmp = self.data.get_table_data_count("district_tmp")
        district_mst = self.data.get_table_data_count("district_mst")
        block_tmp = self.data.get_table_data_count("block_tmp")
        block_mst = self.data.get_table_data_count("block_mst")
        cluster_tmp = self.data.get_table_data_count("cluster_tmp")
        cluster_mst = self.data.get_table_data_count("cluster_mst")
        school_master = self.data.get_table_data_count("school_master")
        school_tmp = self.data.get_table_data_count("school_tmp")
        school_hierarchy_details = self.data.get_table_data_count("school_hierarchy_details")
        school_geo_master = self.data.get_table_data_count("school_geo_master")

        with self.subTest():
            self.assertEqual(district_tmp, 0, "district_tmp data is not deleted")
        with self.subTest():
            self.assertEqual(district_mst, 0, "district_mst data is not deleted")
        with self.subTest():
            self.assertEqual(block_tmp, 0, "block_tmp data is not deleted")
        with self.subTest():
            self.assertEqual(block_mst, 0, "block_mst data is not deleted")
        with self.subTest():
            self.assertEqual(cluster_tmp, 0, "cluster_tmp data is not deleted")
        with self.subTest():
            self.assertEqual(cluster_mst, 0, "cluster_mst data is not deleted")
        with self.subTest():
            self.assertEqual(school_master, 0, "school_master data is not deleted")
        with self.subTest():
            self.assertEqual(school_tmp, 0, "school_tmp data is not deleted")
        with self.subTest():
            self.assertEqual(school_hierarchy_details, 0, "school_hierarchy_details data is not deleted")
        with self.subTest():
            self.assertEqual(school_geo_master, 0, "school_geo_master data is not deleted")



    def test_data_replay_udise(self):
        self.data.select_data_replay_data_source(self.driver, "UDISE")
        time.sleep(2)
        self.data.select_data_replay_year(self.driver, " Delete all data")
        time.sleep(2)
        self.data.click_data_replay_submit_button(self.driver)
        time.sleep(5)
        self.data.click_ok_on_alertbox(self.driver)
        udise_sch_incen_cwsn = self.data.get_table_data_count("udise_sch_incen_cwsn")
        udise_nsqf_plcmnt_c12 = self.data.get_table_data_count("udise_nsqf_plcmnt_c12")
        udise_sch_enr_reptr = self.data.get_table_data_count("udise_sch_enr_reptr")
        udise_nsqf_basic_info = self.data.get_table_data_count("udise_nsqf_basic_info")
        udise_sch_incentives = self.data.get_table_data_count("udise_sch_incentives")
        udise_nsqf_trng_prov = self.data.get_table_data_count("udise_nsqf_trng_prov")
        udise_sch_exmmarks_c10 = self.data.get_table_data_count("udise_sch_exmmarks_c10")
        udise_nsqf_class_cond = self.data.get_table_data_count("udise_nsqf_class_cond")
        udise_school_metrics_trans = self.data.get_table_data_count("udise_school_metrics_trans")
        udise_sch_exmmarks_c12 = self.data.get_table_data_count("udise_sch_exmmarks_c12")
        udise_sch_pgi_details = self.data.get_table_data_count("udise_sch_pgi_details")
        udise_nsqf_enr_caste = self.data.get_table_data_count("udise_nsqf_enr_caste")
        udise_sch_enr_age = self.data.get_table_data_count("udise_sch_enr_age")
        udise_sch_exmres_c10 = self.data.get_table_data_count("udise_sch_exmres_c10")
        udise_sch_profile = self.data.get_table_data_count("udise_sch_profile")
        udise_nsqf_enr_sub_sec = self.data.get_table_data_count("udise_nsqf_enr_sub_sec")
        udise_sch_enr_by_stream = self.data.get_table_data_count("udise_sch_enr_by_stream")
        udise_sch_exmres_c12 = self.data.get_table_data_count("udise_sch_exmres_c12")
        udise_sch_recp_exp = self.data.get_table_data_count("udise_sch_recp_exp")
        udise_nsqf_exmres_c10 = self.data.get_table_data_count("udise_nsqf_exmres_c10")
        udise_sch_enr_cwsn = self.data.get_table_data_count("udise_sch_enr_cwsn")
        udise_sch_exmres_c5 = self.data.get_table_data_count("udise_sch_exmres_c5")
        udise_sch_safety = self.data.get_table_data_count("udise_sch_safety")
        udise_nsqf_exmres_c12 = self.data.get_table_data_count("udise_nsqf_exmres_c12")
        udise_sch_enr_fresh = self.data.get_table_data_count("udise_sch_enr_fresh")
        udise_sch_exmres_c8 = self.data.get_table_data_count("udise_sch_exmres_c8")
        udise_sch_staff_posn = self.data.get_table_data_count("udise_sch_staff_posn")
        udise_nsqf_faculty = self.data.get_table_data_count("udise_nsqf_faculty")
        udise_sch_enr_medinstr = self.data.get_table_data_count("udise_sch_enr_medinstr")
        udise_sch_facility = self.data.get_table_data_count("udise_sch_facility")

        udise_tch_profile = self.data.get_table_data_count("udise_tch_profile")
        udise_nsqf_plcmnt_c10 = self.data.get_table_data_count("udise_nsqf_plcmnt_c10")
        udise_sch_enr_newadm = self.data.get_table_data_count("udise_sch_enr_newadm")





        with self.subTest():
            self.assertEqual(udise_sch_incen_cwsn, 0, "udise_sch_incen_cwsn data is not deleted")
        with self.subTest():
            self.assertEqual(udise_nsqf_plcmnt_c12, 0, "udise_nsqf_plcmnt_c12 data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_enr_reptr, 0, "udise_sch_enr_reptr data is not deleted")
        with self.subTest():
            self.assertEqual(udise_nsqf_basic_info, 0, "udise_nsqf_basic_info data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_incentives, 0, "udise_sch_incentives data is not deleted")
        with self.subTest():
            self.assertEqual(udise_nsqf_trng_prov, 0, "udise_nsqf_trng_prov data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_exmmarks_c10, 0, "udise_sch_exmmarks_c10 data is not deleted")
        with self.subTest():
            self.assertEqual(udise_nsqf_class_cond, 0, "udise_nsqf_class_cond data is not deleted")
        with self.subTest():
            self.assertEqual(udise_school_metrics_trans, 0, "udise_school_metrics_trans data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_exmmarks_c12, 0, "udise_sch_exmmarks_c12 data is not deleted")

        with self.subTest():
            self.assertEqual(udise_sch_pgi_details, 0, "udise_sch_pgi_details data is not deleted")
        with self.subTest():
            self.assertEqual(udise_nsqf_enr_caste, 0, "udise_nsqf_enr_caste data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_enr_age, 0, "udise_sch_enr_age data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_exmres_c10, 0, "udise_sch_exmres_c10 data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_profile, 0, "udise_sch_profile data is not deleted")
        with self.subTest():
            self.assertEqual(udise_nsqf_enr_sub_sec, 0, "udise_nsqf_enr_sub_sec data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_enr_by_stream, 0, "udise_sch_enr_by_stream data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_exmres_c12, 0, "udise_sch_exmres_c12 data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_recp_exp, 0, "udise_sch_recp_exp data is not deleted")
        with self.subTest():
            self.assertEqual(udise_nsqf_exmres_c10, 0, "udise_nsqf_exmres_c10 data is not deleted")

        with self.subTest():
            self.assertEqual(udise_sch_enr_cwsn, 0, "udise_sch_enr_cwsn data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_exmres_c5, 0, "udise_sch_exmres_c5 data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_safety, 0, "udise_sch_safety data is not deleted")
        with self.subTest():
            self.assertEqual(udise_nsqf_exmres_c12, 0, "udise_nsqf_exmres_c12 data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_enr_fresh, 0, "udise_sch_enr_fresh data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_exmres_c8, 0, "udise_sch_exmres_c8 data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_staff_posn, 0, "udise_sch_staff_posn data is not deleted")
        with self.subTest():
            self.assertEqual(udise_nsqf_faculty, 0, "udise_nsqf_faculty data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_enr_medinstr, 0, "udise_sch_enr_medinstr data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_facility, 0, "udise_sch_facility data is not deleted")

        with self.subTest():
            self.assertEqual(udise_tch_profile, 0, "udise_tch_profile data is not deleted")
        with self.subTest():
            self.assertEqual(udise_nsqf_plcmnt_c10, 0, "udise_nsqf_plcmnt_c10 data is not deleted")
        with self.subTest():
            self.assertEqual(udise_sch_enr_newadm, 0, "udise_sch_enr_newadm data is not deleted")

    def test_data_replay_diksha_etb(self):
        self.data.select_data_replay_data_source(self.driver,"Diksha ETB")
        time.sleep(2)
        self.data.pass_from_date_to_diksha_etb_(self.driver)
        self.data.pass_to_date_to_diksha_etb_(self.driver)
        self.data.click_data_replay_submit_button(self.driver)
        time.sleep(5)
        self.data.click_ok_on_alertbox(self.driver)
        diksha_content_staging = self.data.get_table_data_count("diksha_content_staging")
        diksha_content_temp = self.data.get_table_data_count("diksha_content_temp")
        diksha_content_trans = self.data.get_table_data_count("diksha_content_trans")
        diksha_total_content = self.data.get_table_data_count("diksha_total_content")

        with self.subTest():
            self.assertEqual(diksha_content_staging, 0, "diksha_content_staging data is not deleted")
        with self.subTest():
            self.assertEqual(diksha_content_temp, 0, "diksha_content_temp data is not deleted")
        with self.subTest():
            self.assertEqual(diksha_content_trans, 0, "diksha_content_trans data is not deleted")
        with self.subTest():
            self.assertEqual(diksha_total_content, 0, "diksha_total_content data is not deleted")

    def test_data_replay_diksha_tpd(self):
        self.data.select_data_replay_data_source(self.driver, "Diksha TPD")
        time.sleep(2)
        multi_select_button = self.data.click_multi_select_button()
        multi_select_button.click()
        choose_first_option = self.data.select_multi_option_button()
        choose_first_option.click()
        batch_id = "'{}'".format(choose_first_option.text)
        time.sleep(5)
        self.data.click_data_replay_submit_button(self.driver)
        time.sleep(5)
        self.data.click_ok_on_alertbox(self.driver)
        diksha_tpd_trans = self.data.get_table_data_count("diksha_tpd_trans where batch_id = {}".format(batch_id))
        diksha_tpd_content_temp = self.data.get_table_data_count("diksha_tpd_content_temp where batch_id = {}".format(batch_id))
        diksha_tpd_staging = self.data.get_table_data_count("diksha_tpd_staging where batch_id = {}".format(batch_id))

        with self.subTest():
            self.assertEqual(diksha_tpd_trans, 0, "diksha_tpd_trans data is not deleted")
        with self.subTest():
            self.assertEqual(diksha_tpd_content_temp, 0, "diksha_tpd_content_temp data is not deleted")
        with self.subTest():
            self.assertEqual(diksha_tpd_staging, 0, "diksha_tpd_staging data is not deleted")


    def test_data_replay_pat(self):
        self.data.select_data_replay_data_source(self.driver, "PAT")
        time.sleep(2)
        multi_select_button = self.data.click_multi_select_button()
        multi_select_button.click()
        choose_first_option = self.data.select_multi_option_button()
        choose_first_option.click()
        exam_code = "'{}'".format(choose_first_option.text)
        time.sleep(5)
        self.data.click_data_replay_submit_button(self.driver)
        time.sleep(5)
        self.data.click_ok_on_alertbox(self.driver)
        periodic_exam_mst = self.data.get_table_data_count("periodic_exam_mst where exam_code = {}".format(exam_code))
        periodic_exam_result_staging_2 = self.data.get_table_data_count("periodic_exam_result_staging_2 where exam_code = {}".format(exam_code))
        periodic_exam_school_qst_result = self.data.get_table_data_count("periodic_exam_school_qst_result where exam_code = {}".format(exam_code))
        periodic_exam_result_temp = self.data.get_table_data_count("periodic_exam_result_temp where exam_code = {}".format(exam_code))
        periodic_exam_school_result = self.data.get_table_data_count("periodic_exam_school_result where exam_code = {}".format(exam_code))
        periodic_exam_result_staging_1 = self.data.get_table_data_count("periodic_exam_result_staging_1 where exam_code = {}".format(exam_code))
        periodic_exam_result_trans = self.data.get_table_data_count("periodic_exam_result_trans where exam_code = {}".format(exam_code))
        with self.subTest():
            self.assertEqual(periodic_exam_mst, 0, "periodic_exam_mst data is not deleted")
        with self.subTest():
            self.assertEqual(periodic_exam_result_staging_2, 0, "periodic_exam_result_staging_2 data is not deleted")
        with self.subTest():
            self.assertEqual(periodic_exam_school_qst_result, 0, "periodic_exam_school_qst_result data is not deleted")
        with self.subTest():
            self.assertEqual(periodic_exam_result_temp, 0, "periodic_exam_result_temp data is not deleted")
        with self.subTest():
            self.assertEqual(periodic_exam_school_result, 0, "periodic_exam_school_result data is not deleted")
        with self.subTest():
            self.assertEqual(periodic_exam_result_staging_1, 0, "periodic_exam_result_staging_1 data is not deleted")
        with self.subTest():
            self.assertEqual(periodic_exam_result_trans, 0, "periodic_exam_result_trans data is not deleted")

    def test_data_replay_student_attendance(self):
        self.data.select_data_replay_data_source(self.driver,"Student Attendance")
        time.sleep(2)
        year = self.data.get_student_attendance_year()
        self.data.select_data_replay_year(self.driver,year)
        time.sleep(2)
        multi_select_button = self.data.click_multi_select_button()
        multi_select_button.click()
        choose_first_option = self.data.select_multi_option_button()
        choose_first_option.click()
        month = "'{}'".format(choose_first_option.text)
        self.data.click_data_replay_submit_button(self.driver)
        time.sleep(5)
        self.data.click_ok_on_alertbox(self.driver)
        student_attendance_staging_1 = self.data.get_table_data_count("student_attendance_staging_1 where year = {} and month = {}".format(year,month))
        student_attendance_temp = self.data.get_table_data_count(
            "student_attendance_temp where year = {} and month = {}".format(year, month))
        student_attendance_trans = self.data.get_table_data_count(
            "student_attendance_trans where year = {} and month = {}".format(year, month))
        school_student_total_attendance = self.data.get_table_data_count(
            "school_student_total_attendance where year = {} and month = {}".format(year, month))

        with self.subTest():
            self.assertEqual(student_attendance_staging_1, 0, "student_attendance_staging_1 data is not deleted")
        with self.subTest():
            self.assertEqual(student_attendance_temp, 0, "student_attendance_temp data is not deleted")
        with self.subTest():
            self.assertEqual(student_attendance_trans, 0, "student_attendance_trans data is not deleted")
        with self.subTest():
            self.assertEqual(school_student_total_attendance, 0, "school_student_total_attendance data is not deleted")

    def test_data_replay_teacher_attendance(self):
        self.data.select_data_replay_data_source(self.driver, "Teacher Attendance")
        time.sleep(2)
        year = self.data.get_teacher_attendance_year()
        self.data.select_data_replay_year(self.driver, year)
        time.sleep(2)
        multi_select_button = self.data.click_multi_select_button()
        multi_select_button.click()
        choose_first_option = self.data.select_multi_option_button()
        choose_first_option.click()
        month = "'{}'".format(choose_first_option.text)
        self.data.click_data_replay_submit_button(self.driver)
        time.sleep(5)
        self.data.click_ok_on_alertbox(self.driver)
        teacher_attendance_staging_1 = self.data.get_table_data_count(
            "teacher_attendance_staging_1 where year = {} and month = {}".format(year, month))
        teacher_attendance_temp = self.data.get_table_data_count(
            "teacher_attendance_temp where year = {} and month = {}".format(year, month))
        teacher_attendance_trans = self.data.get_table_data_count(
            "teacher_attendance_trans where year = {} and month = {}".format(year, month))
        school_teacher_total_attendance = self.data.get_table_data_count(
            "school_teacher_total_attendance where year = {} and month = {}".format(year, month))

        with self.subTest():
            self.assertEqual(teacher_attendance_staging_1, 0, "teacher_attendance_staging_1 data is not deleted")
        with self.subTest():
            self.assertEqual(teacher_attendance_temp, 0, "teacher_attendance_temp data is not deleted")
        with self.subTest():
            self.assertEqual(teacher_attendance_trans, 0, "teacher_attendance_trans data is not deleted")
        with self.subTest():
            self.assertEqual(school_teacher_total_attendance, 0, "school_teacher_total_attendance data is not deleted")

    def test_data_replay_semester(self):
        self.data.select_data_replay_data_source(self.driver, "Semester")
        time.sleep(2)
        year = self.data.get_semester_academic_year()
        self.data.select_data_replay_year(self.driver, year)
        time.sleep(2)
        multi_select_button = self.data.click_multi_select_button()
        multi_select_button.click()
        choose_first_option = self.data.select_multi_option_button()
        choose_first_option.click()
        semester = "'{}'".format(choose_first_option.text)
        self.data.click_data_replay_submit_button(self.driver)
        time.sleep(5)
        self.data.click_ok_on_alertbox(self.driver)
        semester_exam_mst = self.data.get_table_data_count("semester_exam_mst where semester = {}".format(semester))
        semester_exam_result_staging_2 = self.data.get_table_data_count(
            "semester_exam_result_staging_2 where semester = {}".format(semester))
        semester_exam_school_qst_result = self.data.get_table_data_count(
            "semester_exam_school_qst_result where semester = {}".format(semester))
        semester_exam_result_temp = self.data.get_table_data_count(
            "semester_exam_result_temp where semester = {}".format(semester))
        semester_exam_school_result = self.data.get_table_data_count(
            "semester_exam_school_result where semester = {}".format(semester))
        semester_exam_result_staging_1 = self.data.get_table_data_count(
            "semester_exam_result_staging_1 where semester = {}".format(semester))
        semester_exam_result_trans = self.data.get_table_data_count(
            "semester_exam_result_trans where semester = {}".format(semester))
        with self.subTest():
            self.assertEqual(semester_exam_mst, 0, "semester_exam_mst data is not deleted")
        with self.subTest():
            self.assertEqual(semester_exam_result_staging_2, 0, "semester_exam_result_staging_2 data is not deleted")
        with self.subTest():
            self.assertEqual(semester_exam_school_qst_result, 0, "semester_exam_school_qst_result data is not deleted")
        with self.subTest():
            self.assertEqual(semester_exam_result_temp, 0, "semester_exam_result_temp data is not deleted")
        with self.subTest():
            self.assertEqual(semester_exam_school_result, 0, "semester_exam_school_result data is not deleted")
        with self.subTest():
            self.assertEqual(semester_exam_result_staging_1, 0, "semester_exam_result_staging_1 data is not deleted")
        with self.subTest():
            self.assertEqual(semester_exam_result_trans, 0, "semester_exam_result_trans data is not deleted")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("")