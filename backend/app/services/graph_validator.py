from app.schemas.validation import ValidationIssue, ValidationResult

DATABASE_COMPONENTS = {"postgres", "mongodb", "mysql", "redis"}
ENTRY_COMPONENTS = {"load_balancer", "api_gateway", "cdn"}


class GraphValidator:
    @staticmethod
    def validate(graph):

        issues = []

        GraphValidator._validate_empty_architecture(graph, issues)

        GraphValidator._validate_database_exists(graph, issues)

        GraphValidator._validate_entrypoint_exists(graph, issues)

        GraphValidator._validate_isolated_components(graph, issues)

        return ValidationResult(
            valid=len([i for i in issues if i.severity == "error"]) == 0, issues=issues
        )

    @staticmethod
    def _validate_empty_architecture(graph, issues):

        if len(graph.components) == 0:
            issues.append(
                ValidationIssue(
                    severity="error",
                    code="EMPTY_ARCHITECTURE",
                    message="Architecture contains no components",
                )
            )

    @staticmethod
    def _validate_database_exists(graph, issues):

        found = any(
            component.component_type in DATABASE_COMPONENTS
            for component in graph.components
        )

        if not found:
            issues.append(
                ValidationIssue(
                    severity="warning",
                    code="NO_DATABASE",
                    message="No database component found",
                )
            )

    @staticmethod
    def _validate_entrypoint_exists(graph, issues):

        found = any(
            component.component_type in ENTRY_COMPONENTS
            for component in graph.components
        )

        if not found:
            issues.append(
                ValidationIssue(
                    severity="warning",
                    code="NO_ENTRY_POINT",
                    message="No entry point component found",
                )
            )

    @staticmethod
    def _validate_isolated_components(graph, issues):

        connected = set()

        for connection in graph.connections:
            connected.add(str(connection.source_component_id))

            connected.add(str(connection.target_component_id))

        for component in graph.components:
            if str(component.id) not in connected:
                issues.append(
                    ValidationIssue(
                        severity="warning",
                        code="ISOLATED_COMPONENT",
                        message=f"{component.name} is disconnected",
                    )
                )

    @staticmethod
    def __validate_circular_dependency(graph, issue):
        pass