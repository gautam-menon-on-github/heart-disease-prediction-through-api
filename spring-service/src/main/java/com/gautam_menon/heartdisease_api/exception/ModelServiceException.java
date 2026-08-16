package com.gautam_menon.heartdisease_api.exception;

public class ModelServiceException extends RuntimeException {
    public ModelServiceException(String message, Throwable cause) {
        super(message);
    }
}
