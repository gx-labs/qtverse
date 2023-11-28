// ProSubscription.js

import React from "react";
import styled from "styled-components";

const ProSubscriptionPage = () => {
  return (
    <ProSubscriptionContainer>
      <ProSubscriptionHeader>
        <h1>Upgrade to Pro</h1>
        <p>To copy code of all elements .</p>
      </ProSubscriptionHeader>
      <ProSubscriptionFeatures>
        <FeatureItem>
          <FeatureIcon>&#10003;</FeatureIcon>
          <span>Access to all Widgets.</span>
        </FeatureItem>
        <FeatureItem>
          <FeatureIcon>&#10003;</FeatureIcon>
          <span>Access to Code</span>
        </FeatureItem>
        <FeatureItem>
          <FeatureIcon>&#10003;</FeatureIcon>
          <span>Access to everything !</span>
        </FeatureItem>
        
          
      </ProSubscriptionFeatures>
      <ProSubscriptionPrice>
        <PriceText>500 Rs/month</PriceText>
        <SubscribeButton>Subscribe Now</SubscribeButton>
      </ProSubscriptionPrice>
    </ProSubscriptionContainer>
    
  );
};

// Styled Components
const ProSubscriptionContainer = styled.div`
  max-width: 600px;
  margin: 50px auto;
  padding: 30px;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  background-color: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;

  &:hover {
    transform: scale(1.02);
  }
`;

const ProSubscriptionHeader = styled.div`
  text-align: center;
  margin-bottom: 30px;

  h1 {
    font-size: 2.5em;
    color: #333;
    margin-bottom: 10px;
  }

  p {
    color: #555;
  }
`;

const ProSubscriptionFeatures = styled.div`
  margin-bottom: 60px;
`;

const FeatureItem = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: 15px;

  span {
    margin-left: 15px;
    font-size:20px;
    color: #666;
  }
`;

const FeatureIcon = styled.div`
  font-size: 1.8em;
  color: #4caf50;
`;

const ProSubscriptionPrice = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const PriceText = styled.p`
  font-size: 30px;
  color: #333;
`;

const SubscribeButton = styled.button`
  background-color: #4caf50;
  color: #fff;
  padding: 15px 30px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1.2em;
  transition: background-color 0.3s ease-in-out;

  &:hover {
    background-color: #45a049;
  }
`;

export default ProSubscriptionPage;
