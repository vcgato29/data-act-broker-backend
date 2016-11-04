SELECT award_financial_records.tas,
    award_financial_records.program_activity_code,
    ussgl480100_undelivered_or_fyb_sum_c,
    ussgl480100_undelivered_or_cpe_sum_c,
    ussgl483100_undelivered_or_cpe_sum_c,
    ussgl488100_upward_adjustm_cpe_sum_c,
    obligations_undelivered_or_fyb_sum_c,
    obligations_undelivered_or_cpe_sum_c,
    ussgl490100_delivered_orde_fyb_sum_c,
    ussgl490100_delivered_orde_cpe_sum_c,
    ussgl493100_delivered_orde_cpe_sum_c,
    ussgl498100_upward_adjustm_cpe_sum_c,
    obligations_delivered_orde_fyb_sum_c,
    obligations_delivered_orde_cpe_sum_c,
    ussgl480200_undelivered_or_fyb_sum_c,
    ussgl480200_undelivered_or_cpe_sum_c,
    ussgl483200_undelivered_or_cpe_sum_c,
    ussgl488200_upward_adjustm_cpe_sum_c,
    gross_outlays_undelivered_fyb_sum_c,
    gross_outlays_undelivered_cpe_sum_c,
    ussgl490200_delivered_orde_cpe_sum_c,
    ussgl490800_authority_outl_fyb_sum_c,
    ussgl490800_authority_outl_cpe_sum_c,
    ussgl498200_upward_adjustm_cpe_sum_c,
    gross_outlays_delivered_or_fyb_sum_c,
    gross_outlays_delivered_or_cpe_sum_c,
    gross_outlay_amount_by_awa_fyb_sum_c,
    gross_outlay_amount_by_awa_cpe_sum_c,
    obligations_incurred_byawa_cpe_sum_c,
    ussgl487100_downward_adjus_cpe_sum_c,
    ussgl497100_downward_adjus_cpe_sum_c,
    ussgl487200_downward_adjus_cpe_sum_c,
    ussgl497200_downward_adjus_cpe_sum_c,
    deobligations_recov_by_awa_cpe_sum_c,
    ussgl480100_undelivered_or_fyb_sum_b,
    ussgl480100_undelivered_or_cpe_sum_b,
    ussgl483100_undelivered_or_cpe_sum_b,
    ussgl488100_upward_adjustm_cpe_sum_b,
    obligations_undelivered_or_fyb_sum_b,
    obligations_undelivered_or_cpe_sum_b,
    ussgl490100_delivered_orde_fyb_sum_b,
    ussgl490100_delivered_orde_cpe_sum_b,
    ussgl493100_delivered_orde_cpe_sum_b,
    ussgl498100_upward_adjustm_cpe_sum_b,
    obligations_delivered_orde_fyb_sum_b,
    obligations_delivered_orde_cpe_sum_b,
    ussgl480200_undelivered_or_fyb_sum_b,
    ussgl480200_undelivered_or_cpe_sum_b,
    ussgl483200_undelivered_or_cpe_sum_b,
    ussgl488200_upward_adjustm_cpe_sum_b,
    gross_outlays_undelivered_fyb_sum_b,
    gross_outlays_undelivered_cpe_sum_b,
    ussgl490200_delivered_orde_cpe_sum_b,
    ussgl490800_authority_outl_fyb_sum_b,
    ussgl490800_authority_outl_cpe_sum_b,
    ussgl498200_upward_adjustm_cpe_sum_b,
    gross_outlays_delivered_or_fyb_sum_b,
    gross_outlays_delivered_or_cpe_sum_b,
    gross_outlay_amount_by_pro_fyb_sum_b,
    gross_outlay_amount_by_pro_cpe_sum_b,
    obligations_incurred_by_pr_cpe_sum_b,
    ussgl487100_downward_adjus_cpe_sum_b,
    ussgl497100_downward_adjus_cpe_sum_b,
    ussgl487200_downward_adjus_cpe_sum_b,
    ussgl497200_downward_adjus_cpe_sum_b,
    deobligations_recov_by_pro_cpe_sum_b
FROM (
    SELECT SUM(af.ussgl480100_undelivered_or_fyb) AS ussgl480100_undelivered_or_fyb_sum_c,
        SUM(af.ussgl480100_undelivered_or_cpe) AS ussgl480100_undelivered_or_cpe_sum_c,
        SUM(af.ussgl483100_undelivered_or_cpe) AS ussgl483100_undelivered_or_cpe_sum_c,
        SUM(af.ussgl488100_upward_adjustm_cpe) AS ussgl488100_upward_adjustm_cpe_sum_c,
        SUM(af.obligations_undelivered_or_fyb) AS obligations_undelivered_or_fyb_sum_c,
        SUM(af.obligations_undelivered_or_cpe) AS obligations_undelivered_or_cpe_sum_c,
        SUM(af.ussgl490100_delivered_orde_fyb) AS ussgl490100_delivered_orde_fyb_sum_c,
        SUM(af.ussgl490100_delivered_orde_cpe) AS ussgl490100_delivered_orde_cpe_sum_c,
        SUM(af.ussgl493100_delivered_orde_cpe) AS ussgl493100_delivered_orde_cpe_sum_c,
        SUM(af.ussgl498100_upward_adjustm_cpe) AS ussgl498100_upward_adjustm_cpe_sum_c,
        SUM(af.obligations_delivered_orde_fyb) AS obligations_delivered_orde_fyb_sum_c,
        SUM(af.obligations_delivered_orde_cpe) AS obligations_delivered_orde_cpe_sum_c,
        SUM(af.ussgl480200_undelivered_or_fyb) AS ussgl480200_undelivered_or_fyb_sum_c,
        SUM(af.ussgl480200_undelivered_or_cpe) AS ussgl480200_undelivered_or_cpe_sum_c,
        SUM(af.ussgl483200_undelivered_or_cpe) AS ussgl483200_undelivered_or_cpe_sum_c,
        SUM(af.ussgl488200_upward_adjustm_cpe) AS ussgl488200_upward_adjustm_cpe_sum_c,
        SUM(af.gross_outlays_undelivered_fyb) AS gross_outlays_undelivered_fyb_sum_c,
        SUM(af.gross_outlays_undelivered_cpe) AS gross_outlays_undelivered_cpe_sum_c,
        SUM(af.ussgl490200_delivered_orde_cpe) AS ussgl490200_delivered_orde_cpe_sum_c,
        SUM(af.ussgl490800_authority_outl_fyb) AS ussgl490800_authority_outl_fyb_sum_c,
        SUM(af.ussgl490800_authority_outl_cpe) AS ussgl490800_authority_outl_cpe_sum_c,
        SUM(af.ussgl498200_upward_adjustm_cpe) AS ussgl498200_upward_adjustm_cpe_sum_c,
        SUM(af.gross_outlays_delivered_or_fyb) AS gross_outlays_delivered_or_fyb_sum_c,
        SUM(af.gross_outlays_delivered_or_cpe) AS gross_outlays_delivered_or_cpe_sum_c,
        SUM(af.gross_outlay_amount_by_awa_fyb) AS gross_outlay_amount_by_awa_fyb_sum_c,
        SUM(af.gross_outlay_amount_by_awa_cpe) AS gross_outlay_amount_by_awa_cpe_sum_c,
        SUM(af.obligations_incurred_byawa_cpe) AS obligations_incurred_byawa_cpe_sum_c,
        SUM(af.ussgl487100_downward_adjus_cpe) AS ussgl487100_downward_adjus_cpe_sum_c,
        SUM(af.ussgl497100_downward_adjus_cpe) AS ussgl497100_downward_adjus_cpe_sum_c,
        SUM(af.ussgl487200_downward_adjus_cpe) AS ussgl487200_downward_adjus_cpe_sum_c,
        SUM(af.ussgl497200_downward_adjus_cpe) AS ussgl497200_downward_adjus_cpe_sum_c,
        SUM(af.deobligations_recov_by_awa_cpe) AS deobligations_recov_by_awa_cpe_sum_c,
        af.tas,
        af.program_activity_code
    FROM award_financial AS af
    WHERE af.submission_id = {0}
    GROUP BY af.tas,
        af.program_activity_code,
        af.submission_id
) AS award_financial_records
FULL OUTER JOIN
(
    SELECT SUM(op.ussgl480100_undelivered_or_fyb) AS ussgl480100_undelivered_or_fyb_sum_b,
        SUM(op.ussgl480100_undelivered_or_cpe) AS ussgl480100_undelivered_or_cpe_sum_b,
        SUM(op.ussgl483100_undelivered_or_cpe) AS ussgl483100_undelivered_or_cpe_sum_b,
        SUM(op.ussgl488100_upward_adjustm_cpe) AS ussgl488100_upward_adjustm_cpe_sum_b,
        SUM(op.obligations_undelivered_or_fyb) AS obligations_undelivered_or_fyb_sum_b,
        SUM(op.obligations_undelivered_or_cpe) AS obligations_undelivered_or_cpe_sum_b,
        SUM(op.ussgl490100_delivered_orde_fyb) AS ussgl490100_delivered_orde_fyb_sum_b,
        SUM(op.ussgl490100_delivered_orde_cpe) AS ussgl490100_delivered_orde_cpe_sum_b,
        SUM(op.ussgl493100_delivered_orde_cpe) AS ussgl493100_delivered_orde_cpe_sum_b,
        SUM(op.ussgl498100_upward_adjustm_cpe) AS ussgl498100_upward_adjustm_cpe_sum_b,
        SUM(op.obligations_delivered_orde_fyb) AS obligations_delivered_orde_fyb_sum_b,
        SUM(op.obligations_delivered_orde_cpe) AS obligations_delivered_orde_cpe_sum_b,
        SUM(op.ussgl480200_undelivered_or_fyb) AS ussgl480200_undelivered_or_fyb_sum_b,
        SUM(op.ussgl480200_undelivered_or_cpe) AS ussgl480200_undelivered_or_cpe_sum_b,
        SUM(op.ussgl483200_undelivered_or_cpe) AS ussgl483200_undelivered_or_cpe_sum_b,
        SUM(op.ussgl488200_upward_adjustm_cpe) AS ussgl488200_upward_adjustm_cpe_sum_b,
        SUM(op.gross_outlays_undelivered_fyb) AS gross_outlays_undelivered_fyb_sum_b,
        SUM(op.gross_outlays_undelivered_cpe) AS gross_outlays_undelivered_cpe_sum_b,
        SUM(op.ussgl490200_delivered_orde_cpe) AS ussgl490200_delivered_orde_cpe_sum_b,
        SUM(op.ussgl490800_authority_outl_fyb) AS ussgl490800_authority_outl_fyb_sum_b,
        SUM(op.ussgl490800_authority_outl_cpe) AS ussgl490800_authority_outl_cpe_sum_b,
        SUM(op.ussgl498200_upward_adjustm_cpe) AS ussgl498200_upward_adjustm_cpe_sum_b,
        SUM(op.gross_outlays_delivered_or_fyb) AS gross_outlays_delivered_or_fyb_sum_b,
        SUM(op.gross_outlays_delivered_or_cpe) AS gross_outlays_delivered_or_cpe_sum_b,
        SUM(op.gross_outlay_amount_by_pro_fyb) AS gross_outlay_amount_by_pro_fyb_sum_b,
        SUM(op.gross_outlay_amount_by_pro_cpe) AS gross_outlay_amount_by_pro_cpe_sum_b,
        SUM(op.obligations_incurred_by_pr_cpe) AS obligations_incurred_by_pr_cpe_sum_b,
        SUM(op.ussgl487100_downward_adjus_cpe) AS ussgl487100_downward_adjus_cpe_sum_b,
        SUM(op.ussgl497100_downward_adjus_cpe) AS ussgl497100_downward_adjus_cpe_sum_b,
        SUM(op.ussgl487200_downward_adjus_cpe) AS ussgl487200_downward_adjus_cpe_sum_b,
        SUM(op.ussgl497200_downward_adjus_cpe) AS ussgl497200_downward_adjus_cpe_sum_b,
        SUM(op.deobligations_recov_by_pro_cpe) AS deobligations_recov_by_pro_cpe_sum_b,
        op.tas,
        op.program_activity_code
    FROM object_class_program_activity AS op
    WHERE op.submission_id = {0}
    GROUP BY op.tas,
        op.program_activity_code,
        op.submission_id
) AS object_class_records
    ON object_class_records.tas = award_financial_records.tas
        AND object_class_records.program_activity_code = award_financial_records.program_activity_code
WHERE (ussgl480100_undelivered_or_fyb_sum_c < ussgl480100_undelivered_or_fyb_sum_b
    OR ussgl480100_undelivered_or_cpe_sum_c < ussgl480100_undelivered_or_cpe_sum_b
    OR ussgl483100_undelivered_or_cpe_sum_c < ussgl483100_undelivered_or_cpe_sum_b
    OR ussgl488100_upward_adjustm_cpe_sum_c < ussgl488100_upward_adjustm_cpe_sum_b
    OR obligations_undelivered_or_fyb_sum_c < obligations_undelivered_or_fyb_sum_b
    OR obligations_undelivered_or_cpe_sum_c < obligations_undelivered_or_cpe_sum_b
    OR ussgl490100_delivered_orde_fyb_sum_c < ussgl490100_delivered_orde_fyb_sum_b
    OR ussgl490100_delivered_orde_cpe_sum_c < ussgl490100_delivered_orde_cpe_sum_b
    OR ussgl493100_delivered_orde_cpe_sum_c < ussgl493100_delivered_orde_cpe_sum_b
    OR ussgl498100_upward_adjustm_cpe_sum_c < ussgl498100_upward_adjustm_cpe_sum_b
    OR obligations_delivered_orde_fyb_sum_c < obligations_delivered_orde_fyb_sum_b
    OR obligations_delivered_orde_cpe_sum_c < obligations_delivered_orde_cpe_sum_b
    OR ussgl480200_undelivered_or_fyb_sum_c < ussgl480200_undelivered_or_fyb_sum_b
    OR ussgl480200_undelivered_or_cpe_sum_c < ussgl480200_undelivered_or_cpe_sum_b
    OR ussgl483200_undelivered_or_cpe_sum_c < ussgl483200_undelivered_or_cpe_sum_b
    OR ussgl488200_upward_adjustm_cpe_sum_c < ussgl488200_upward_adjustm_cpe_sum_b
    OR gross_outlays_undelivered_fyb_sum_c < gross_outlays_undelivered_fyb_sum_b
    OR gross_outlays_undelivered_cpe_sum_c < gross_outlays_undelivered_cpe_sum_b
    OR ussgl490200_delivered_orde_cpe_sum_c < ussgl490200_delivered_orde_cpe_sum_b
    OR ussgl490800_authority_outl_fyb_sum_c < ussgl490800_authority_outl_fyb_sum_b
    OR ussgl490800_authority_outl_cpe_sum_c < ussgl490800_authority_outl_cpe_sum_b
    OR ussgl498200_upward_adjustm_cpe_sum_c < ussgl498200_upward_adjustm_cpe_sum_b
    OR gross_outlays_delivered_or_fyb_sum_c < gross_outlays_delivered_or_fyb_sum_b
    OR gross_outlays_delivered_or_cpe_sum_c < gross_outlays_delivered_or_cpe_sum_b
    OR gross_outlay_amount_by_awa_fyb_sum_c < gross_outlay_amount_by_pro_fyb_sum_b
    OR gross_outlay_amount_by_awa_cpe_sum_c < gross_outlay_amount_by_pro_cpe_sum_b
    OR obligations_incurred_byawa_cpe_sum_c < obligations_incurred_by_pr_cpe_sum_b
    OR ussgl487100_downward_adjus_cpe_sum_c < ussgl487100_downward_adjus_cpe_sum_b
    OR ussgl497100_downward_adjus_cpe_sum_c < ussgl497100_downward_adjus_cpe_sum_b
    OR ussgl487200_downward_adjus_cpe_sum_c < ussgl487200_downward_adjus_cpe_sum_b
    OR ussgl497200_downward_adjus_cpe_sum_c < ussgl497200_downward_adjus_cpe_sum_b
    OR deobligations_recov_by_awa_cpe_sum_c < deobligations_recov_by_pro_cpe_sum_b);