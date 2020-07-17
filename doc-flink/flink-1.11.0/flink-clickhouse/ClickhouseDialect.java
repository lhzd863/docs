package org.apache.flink.connector.jdbc.dialect;

import org.apache.flink.connector.jdbc.internal.converter.ClickhouseRowConverter;
import org.apache.flink.connector.jdbc.internal.converter.JdbcRowConverter;
import org.apache.flink.table.types.logical.LogicalTypeRoot;
import org.apache.flink.table.types.logical.RowType;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

class ClickhouseDialect extends AbstractDialect {

        private static final long serialVersionUID = 1L;

        // Define MAX/MIN precision of TIMESTAMP type according to derby docs:
        // http://db.apache.org/derby/docs/10.14/ref/rrefsqlj27620.html
        private static final int MAX_TIMESTAMP_PRECISION = 9;
        private static final int MIN_TIMESTAMP_PRECISION = 1;

        // Define MAX/MIN precision of DECIMAL type according to derby docs:
        // http://db.apache.org/derby/docs/10.14/ref/rrefsqlj15260.html
        private static final int MAX_DECIMAL_PRECISION = 31;
        private static final int MIN_DECIMAL_PRECISION = 1;

        @Override
        public boolean canHandle(String url) {
                return url.startsWith("jdbc:clickhouse:");
        }

        @Override
        public JdbcRowConverter getRowConverter(RowType rowType) {
                return new ClickhouseRowConverter(rowType);
        }

        @Override
        public Optional<String> defaultDriverName() {
                return Optional.of("ru.yandex.clickhouse.ClickHouseDriver");
        }

        @Override
        public Optional<String> getUpsertStatement(String tableName, String[] fieldNames, String[] uniqueKeyFields) {
                return Optional.of(getInsertIntoStatement(tableName, fieldNames));
        }

        @Override
        public String getUpdateStatement(String tableName, String[] fieldNames, String[] conditionFields) {
                return null;
        }

        @Override
        public String getDeleteStatement(String tableName, String[] conditionFields) {
                return getInsertIntoStatement(tableName, conditionFields);
        }

        @Override
        public String quoteIdentifier(String identifier) {
                return identifier;
        }

        @Override
        public String dialectName() {
                return "Clickhouse";
        }

        @Override
        public int maxDecimalPrecision() {
                return MAX_DECIMAL_PRECISION;
        }

        @Override
        public int minDecimalPrecision() {
                return MIN_DECIMAL_PRECISION;
        }

        @Override
        public int maxTimestampPrecision() {
                return MAX_TIMESTAMP_PRECISION;
        }

        @Override
        public int minTimestampPrecision() {
                return MIN_TIMESTAMP_PRECISION;
        }

        @Override
        public List<LogicalTypeRoot> unsupportedTypes() {
                // The data types used in Derby are list at
                // http://db.apache.org/derby/docs/10.14/ref/crefsqlj31068.html

                // TODO: We can't convert BINARY data type to
                //  PrimitiveArrayTypeInfo.BYTE_PRIMITIVE_ARRAY_TYPE_INFO in LegacyTypeInfoDataTypeConverter.
                return Arrays.asList(
                        LogicalTypeRoot.BINARY,
                        LogicalTypeRoot.TIMESTAMP_WITH_LOCAL_TIME_ZONE,
                        LogicalTypeRoot.TIMESTAMP_WITH_TIME_ZONE,
                        LogicalTypeRoot.INTERVAL_YEAR_MONTH,
                        LogicalTypeRoot.INTERVAL_DAY_TIME,
                        LogicalTypeRoot.ARRAY,
                        LogicalTypeRoot.MULTISET,
                        LogicalTypeRoot.MAP,
                        LogicalTypeRoot.ROW,
                        LogicalTypeRoot.DISTINCT_TYPE,
                        LogicalTypeRoot.STRUCTURED_TYPE,
                        LogicalTypeRoot.NULL,
                        LogicalTypeRoot.RAW,
                        LogicalTypeRoot.SYMBOL,
                        LogicalTypeRoot.UNRESOLVED);
        }
}
