-- A380_Admin_data context user ID and all context user insertion

DECLARE @CONTEXT_id INT

SELECT @CONTEXT_id = CONTEXT_id FROM T_EDIP_CONTEXT WHERE ContextName='A400M_Admin_data'


IF NOT EXISTS(SELECT * FROM T_LINK_CONTEXT__USER WHERE CONTEXT__USER_CONTEXT_idr=@CONTEXT_id)
BEGIN
INSERT INTO T_LINK_CONTEXT__USER (
CONTEXT__USER_CONTEXT_idr,
CONTEXT__USER_USER_idr
) SELECT DISTINCT @CONTEXT_id, 
         CONTEXT__USER_USER_idr
  FROM T_EDIP_CONTEXT,T_LINK_CONTEXT__USER
  WHERE CONTEXT__USER_CONTEXT_idr = CONTEXT_id
  AND ContextName IN ('Admin','Admin_SYSTEM','A400M_Support')
;
END
