package com.gautam_menon.heartdisease_api.dto;

import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Pattern;
import lombok.*;

@Data
public class HeartDiseaseApiRequest {

    @NotNull @Min(1) @Max(120)
    private Integer age;

    @NotNull @Pattern(regexp = "M|F", message = "sex must be M or F")
    private String sex;

    @NotNull @Pattern(regexp = "TA|ATA|NAP|ASY", message = "invalid chest_pain_type")
    private String chestPainType;

    @NotNull @Min(0)
    private Integer restingBp;

    @NotNull @Min(0)
    private Integer cholesterol;

    @NotNull @Min(0) @Max(1)
    private Integer fastingBs;

    @NotNull @Pattern(regexp = "Normal|ST|LVH", message = "invalid resting_ecg")
    private String restingEcg;

    @NotNull @Min(60) @Max(202)
    private Integer maxHr;

    @NotNull @Pattern(regexp = "Y|N", message = "exercise_angina must be Y or N")
    private String exerciseAngina;

    @NotNull @Min(0)
    private Double oldpeak;

    @NotNull @Pattern(regexp = "Up|Flat|Down", message = "invalid st_slope")
    private String stSlope;
}
